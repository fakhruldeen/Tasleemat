from setuptools import setup, find_packages

setup(
    name="tasleemat",
    version="2.2.0",
    description="Enterprise Bilingual (English & Arabic) Project Management & AI Automation Library",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "tasleemat": [
            "forms/**/*", 
            "docs/**/*", 
            "_tokens/**/*"
        ]
    },
    entry_points={
        "console_scripts": [
            "tasleemat=tasleemat.tools.tasleemat_cli:main",
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
)
