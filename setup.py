import setuptools
import sys
import os
import shutil
import glob
import subprocess

from distutils.command.sdist import sdist

# This directory
dir_setup = os.path.dirname(os.path.realpath(__file__))


with open("similab\README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="similab", #Este es el nombre que figura en PyPI
    version="0.0.5.16dev",
    author="CID",
    author_email="author@example.com",
    description="NPL Package in development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='NLP corpus meaning',
    url="https://github.com/CID-ITBA",
    packages=["similab"],#setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'numpy',
          'scipy',
      ],
    python_requires='>=3.6',
)