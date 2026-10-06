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
cp ../../LICENSE .
# Do not overwrite the SDK README.md

# Create init files
touch tasleemat/__init__.py
touch tasleemat/tools/__init__.py
touch tasleemat/tools/attested_computations/__init__.py

echo "Building Python package..."
../../.venv/bin/python -m build

echo "Build complete! Artifacts are in sdk/python/dist/"
