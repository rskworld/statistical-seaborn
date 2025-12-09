"""
Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Project: Statistical Data Analysis with Seaborn

Setup script for the Statistical Data Analysis with Seaborn project.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="statistical-seaborn",
    version="1.0.0",
    author="RSK World",
    author_email="help@rskworld.in",
    description="Comprehensive statistical visualization project with advanced plotting techniques using Seaborn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://rskworld.in",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)

