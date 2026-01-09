#!/bin/bash
# Backend startup script

cd "$(dirname "$0")"

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "Error: .env file not found"
    echo "Please copy .env.example to .env and configure your settings"
    echo "  cp .env.example .env"
    exit 1
fi

# Check if HEPAI_API_KEY is set (either in .env or environment)
if [ -z "$HEPAI_API_KEY" ] && grep -q "^HEPAI_API_KEY=your_api_key_here" .env 2>/dev/null; then
    echo "Warning: HEPAI_API_KEY is not configured"
    echo "Please set it in environment variable or .env file"
    echo ""
elif [ -n "$HEPAI_API_KEY" ]; then
    echo "✓ HEPAI_API_KEY loaded from environment variable"
fi

echo "Starting HaiNougat Backend Server..."
echo "Server will be available at: http://localhost:8000"
echo "API Documentation: http://localhost:8000/api/v1/docs"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

python -m app.main
