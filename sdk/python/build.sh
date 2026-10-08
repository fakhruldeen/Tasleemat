#!/bin/bash
set -e

echo "Setting up SDK build environment..."
rm -rf tasleemat
mkdir -p tasleemat

echo "Copying repository assets..."
cp -r ../../forms tasleemat/
cp -r ../../docs tasleemat/
cp -r ../../_tokens tasleemat/
cp -r ../../tools tasleemat/
cp -r ../../tools/ai tasleemat/ai
cp ../../LICENSE .
# Do not overwrite the SDK README.md

# Create init files
touch tasleemat/__init__.py
touch tasleemat/tools/__init__.py
touch tasleemat/tools/attested_computations/__init__.py

PYTHON_BIN="python3"
if [ -f "../../sdk_test_venv/bin/python" ]; then
    PYTHON_BIN="../../sdk_test_venv/bin/python"
elif [ -f "../../.venv/bin/python" ]; then
    PYTHON_BIN="../../.venv/bin/python"
fi

$PYTHON_BIN -m build

echo "Build complete! Artifacts are in sdk/python/dist/"
