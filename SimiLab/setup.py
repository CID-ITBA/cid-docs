import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SimLab", #Este es el nombre que figura en PyPI
    version="0.0.1",
    author="CID",
    author_email="author@example.com",
    description="NPL Package in development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='NLP corpus meaning',
    url="https://github.com/CID-ITBA",
    packages=setuptools.find_packages(),
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