#!/bin/bash
# Frontend startup script

cd "$(dirname "$0")"

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "Dependencies not installed. Installing..."
    npm install
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "Warning: .env file not found, using defaults"
    echo "You can copy .env.example to .env to customize settings"
    echo ""
fi

echo "Starting HaiNougat Frontend Development Server..."
echo "Frontend will be available at: http://localhost:3000"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

npm start
