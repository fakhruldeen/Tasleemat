#!/bin/bash
set -e

if [ ! -d "dist" ]; then
    echo "Error: dist/ directory not found. Please run ./build.sh first."
    exit 1
fi

echo "========================================="
echo "🚀 Publishing Tasleemat to PyPI"
echo "========================================="
echo "If you haven't already, please create an API token on PyPI:"
echo "1. Go to https://pypi.org/manage/account/token/"
echo "2. Click 'Add API token'"
echo "3. Copy the token (it starts with pypi-)"
echo "-----------------------------------------"

read -p "Enter your PyPI API token (or press Ctrl+C to abort): " PYPI_TOKEN

if [ -z "$PYPI_TOKEN" ]; then
    echo "Token cannot be empty. Aborting."
    exit 1
fi

echo "Installing twine..."
../../.venv/bin/python -m pip install --upgrade twine

echo "Uploading to PyPI..."
TWINE_USERNAME="__token__" TWINE_PASSWORD="$PYPI_TOKEN" ../../.venv/bin/python -m twine upload dist/*

echo "✅ Successfully published to PyPI!"
