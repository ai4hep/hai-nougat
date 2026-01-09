#!/usr/bin/env python
"""
HepAI API Connection Test Script
Tests connectivity and authentication to HepAI API
"""

import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hai_model import HaiModel

def test_api_connection():
    """Test HepAI API connection"""

    print("=" * 60)
    print("HepAI API Connection Test")
    print("=" * 60)

    # Check API key
    api_key = os.environ.get("HEPAI_API_KEY")
    if not api_key:
        print("❌ HEPAI_API_KEY not found in environment variables")
        print("\nPlease set it in your bashrc:")
        print("  export HEPAI_API_KEY='your_api_key_here'")
        print("  source ~/.bashrc")
        return False

    print(f"✓ API Key found: {api_key[:10]}...")
    print()

    # Test 1: List models
    print("Test 1: Listing available models...")
    try:
        models = HaiModel.list(
            api_key=api_key,
            url="https://aiapi.ihep.ac.cn:42901"
        )
        print(f"✓ Successfully connected to HepAI API")
        print(f"✓ Found {len(models.get('models', []))} models")

        if 'hepai/hainougat' in models.get('models', []):
            print("✓ hainougat model is available")
        else:
            print("⚠ hainougat model not found in available models")
            print(f"Available models: {models.get('models', [])}")

        print()
        return True

    except Exception as e:
        print(f"❌ Failed to connect to HepAI API")
        print(f"Error: {str(e)}")
        print()
        return False

def test_inference(test_pdf=None):
    """Test inference call (requires a test PDF)"""

    if not test_pdf or not os.path.exists(test_pdf):
        print("Test 2: Skipping inference test (no test PDF provided)")
        print()
        return

    print("Test 2: Testing inference with sample PDF...")

    try:
        api_key = os.environ.get("HEPAI_API_KEY")
        result = HaiModel.inference(
            model='hepai/hainougat',
            timeout=3000,
            stream=False,
            pdf_path=test_pdf,
            url="https://aiapi.ihep.ac.cn",
            api_key=api_key
        )

        print(f"✓ Inference successful")
        print(f"Result preview: {result[:200]}...")
        print()
        return True

    except Exception as e:
        print(f"❌ Inference failed")
        print(f"Error: {str(e)}")
        print()
        return False

def main():
    # Test basic connection
    connection_ok = test_api_connection()

    # Optionally test inference if PDF path provided
    if len(sys.argv) > 1:
        test_pdf = sys.argv[1]
        test_inference(test_pdf)

    print("=" * 60)
    if connection_ok:
        print("✓ API connection test passed")
        print("\nYour backend should be able to connect to HepAI API")
    else:
        print("❌ API connection test failed")
        print("\nPlease fix the issues above before using the backend")
    print("=" * 60)

if __name__ == "__main__":
    main()
