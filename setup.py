from setuptools import setup, find_packages
import codecs
import os

VERSION = "0.0.3"
DESCRIPTION = "Samay"
LONG_DESCRIPTION = "A packay to find out execution time of a function, or compare two function with respect to execution time."

# Setting up
setup(
    name="Samay",
    version=VERSION,
    author="Saurav Sharma",
    author_email="sv19projects@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[""],
    keywords=["Samay","samay","time","execution","execution time","run time","runtime","function runtime","function execution time","compare function"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)