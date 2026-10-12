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

if [ -z "$PYPI_TOKEN" ]; then
    read -p "Enter your PyPI API token (or press Ctrl+C to abort): " PYPI_TOKEN
fi

if [ -z "$PYPI_TOKEN" ]; then
    echo "Token cannot be empty. Aborting."
    exit 1
fi

TWINE_BIN="twine"
if ! command -v twine &> /dev/null; then
    TWINE_BIN="python3 -m twine"
fi

echo "Verifying package metadata..."
$TWINE_BIN check dist/*2.4.1*

echo "Uploading v2.4.1 to PyPI..."
TWINE_USERNAME="__token__" TWINE_PASSWORD="$PYPI_TOKEN" $TWINE_BIN upload dist/*2.4.1* --skip-existing

echo "✅ Successfully published Tasleemat v2.4.1 to PyPI!"
