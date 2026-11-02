#!/usr/bin/env python3
"""Setup script for OSCA.

Origin, Semantic, and Consequence Authority:
A Multi-Tier Authorization Architecture for Autonomous AI Agents.
Scope: Python 3.11+.

No PyPI distribution at the research-draft stage.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

try:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [
            line.strip()
            for line in fh
            if line.strip() and not line.startswith("#")
        ]
except FileNotFoundError:
    requirements = ["pydantic>=2.0.0"]

setup(
    name="osca-engine",
    version="1.0.0",
    author="Samir Baladi",
    author_email="gitdeeper@gmail.com",
    description=(
        "OSCA: Origin, Semantic, and Consequence Authority — "
        "A Multi-Tier Authorization Architecture for Autonomous AI Agents"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "docs.*"]),
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=4.1.0",
            "black>=24.0.0",
            "flake8>=7.0.0",
            "mypy>=1.8.0",
            "isort>=5.13.0",
            "pre-commit>=3.6.0",
        ],
    },
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Security",
    ],
    keywords=(
        "multi-tier authorization, autonomous agents, ai governance, "
        "execution binding, decision traceability, semantic governance"
    ),
)
