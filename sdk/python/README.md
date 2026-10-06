<!--
---
type: Guide
---
-->
# Tasleemat Python SDK

This directory contains the Python packaging pipeline for the **Tasleemat** PMO Governance & Quality Assurance framework.

The build scripts in this folder transform the open-source Markdown template repository into a fully compliant, pip-installable Python package, giving users access to the global `tasleemat` CLI scaffolding tool.

## Build Requirements
- Python 3.9+
- `build` module (`pip install build`)

## How to Build
Because Tasleemat acts primarily as a data-first GitHub template library, the actual source files (`forms/`, `docs/`, `tools/`) reside in the root of the repository.

To build the Python SDK, run the included build script. This will temporarily copy the necessary assets from the repository root into a localized package namespace before building the wheel:

```bash
cd sdk/python
./build.sh
```

## Build Artifacts
Upon a successful build, the `.whl` and `.tar.gz` distribution files will be located in the newly created `dist/` directory:

```bash
ls -l dist/
```

## How to Install Locally
You can install the compiled wheel into your local environment (or any virtual environment) to test the CLI tool:

```bash
pip install dist/tasleemat-2.0.3-py3-none-any.whl
```

## Usage
Once installed, the `tasleemat` CLI is globally accessible on your terminal. You can use it to instantly scaffold complete PMO project workspaces out of the bundled OKF templates:

```bash
# List all available deliverables in English
tasleemat list --lang en

# Initialize a new Tier 1 Agile project workspace
tasleemat init --tier 1 --pack agile --lang both --name "My_Project" --code "PRJ-001" --out ./workspace
```
