#!/bin/bash

# HaiNougat Checkpoint Download Script
# Downloads and extracts the checkpoint from IHEP Box

set -e  # Exit on error

echo "============================================"
echo "HaiNougat Checkpoint Download Script"
echo "============================================"

# Configuration
# DOWNLOAD_URL="https://ihepbox.ihep.ac.cn/ihepbox/index.php/s/0ozLQdew0PcyiFV/download"
DOWNLOAD_URL="https://ihepbox.ihep.ac.cn/ihepbox/index.php/s/5LFkBKQjOx9dKL9/download"
WORKER_DIR="$(cd "$(dirname "$0")" && pwd)"
CHECKPOINT_DIR="${WORKER_DIR}/checkpoint"
ZIP_FILE="${WORKER_DIR}/checkpoint.zip"

echo "Worker directory: ${WORKER_DIR}"
echo "Checkpoint will be saved to: ${CHECKPOINT_DIR}"
echo ""

# Check if checkpoint already exists
if [ -d "${CHECKPOINT_DIR}" ]; then
    echo "WARNING: Checkpoint directory already exists at ${CHECKPOINT_DIR}"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 0
    fi
    echo "Removing existing checkpoint..."
    rm -rf "${CHECKPOINT_DIR}"
fi

# Download checkpoint
echo "Downloading checkpoint from IHEP Box..."
echo "URL: ${DOWNLOAD_URL}"
if command -v wget &> /dev/null; then
    wget -O "${ZIP_FILE}" "${DOWNLOAD_URL}" --show-progress
elif command -v curl &> /dev/null; then
    curl -L -o "${ZIP_FILE}" "${DOWNLOAD_URL}" --progress-bar
else
    echo "ERROR: Neither wget nor curl is available. Please install one of them."
    exit 1
fi

echo ""
echo "Download completed!"
echo ""

# Verify the downloaded file
if [ ! -f "${ZIP_FILE}" ]; then
    echo "ERROR: Downloaded file not found at ${ZIP_FILE}"
    exit 1
fi

FILE_SIZE=$(du -h "${ZIP_FILE}" | cut -f1)
echo "Downloaded file size: ${FILE_SIZE}"

# Extract checkpoint
echo "Extracting checkpoint..."
if command -v unzip &> /dev/null; then
    unzip -q "${ZIP_FILE}" -d "${WORKER_DIR}"
    echo "Extraction completed!"
else
    echo "ERROR: unzip is not available. Please install unzip."
    exit 1
fi

# Clean up zip file
echo ""
read -p "Do you want to delete the zip file? (Y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    rm "${ZIP_FILE}"
    echo "Zip file deleted."
else
    echo "Zip file kept at: ${ZIP_FILE}"
fi

echo ""
echo "============================================"
echo "✓ Checkpoint setup completed!"
echo "============================================"
echo ""
echo "Checkpoint location: ${CHECKPOINT_DIR}"
echo ""
# echo "To use this checkpoint, set the environment variable:"
# echo "  export NOUGAT_CHECKPOINT=\"${CHECKPOINT_DIR}\""
# echo ""
# echo "Or add it to your ~/.bashrc or ~/.zshrc:"
# echo "  echo 'export NOUGAT_CHECKPOINT=\"${CHECKPOINT_DIR}\"' >> ~/.bashrc"
# echo ""
