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
cp ../../README.md .
cp ../../LICENSE .
cp ../../RELEASE_NOTES.md .

# Create init files
touch tasleemat/__init__.py
touch tasleemat/tools/__init__.py
touch tasleemat/tools/attested_computations/__init__.py

# Update the tasleemat_cli.py path resolution
# From: ROOT = pathlib.Path(__file__).resolve().parent.parent
# To: ROOT = pathlib.Path(__file__).resolve().parent.parent
# Wait! Parent of tasleemat_cli.py is tools. Parent of tools is tasleemat.
# Inside tasleemat, we have forms. So parent.parent is exactly tasleemat!
# No change needed!

echo "Building Python package..."
../../.venv/bin/python -m build

echo "Build complete! Artifacts are in sdk/python/dist/"
