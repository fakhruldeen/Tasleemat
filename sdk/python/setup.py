from setuptools import setup, find_packages

setup(
    name="tasleemat",
    version="2.5.0",
    description="Enterprise Bilingual (English & Arabic) Project Management & AI Automation Library",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "tasleemat": [
            "forms/**/*", 
            "docs/**/*", 
            "_tokens/**/*",
            "data/**/*",
            "schemas/**/*"
        ]
    },
    entry_points={
        "console_scripts": [
            "tasleemat=tasleemat.tools.tasleemat_cli:main",
            "tasleemat-mcp=tasleemat.mcp.server:main",
        ]
    },
    install_requires=[
        "mkdocs>=1.6.0",
        "mkdocs-material>=9.5.0",
        "pymdown-extensions>=10.7.0",
        "frictionless>=5.18.0",
        "tiktoken",
        "numpy"
    ],
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Financial :: Point-Of-Sale",
    ],
)
