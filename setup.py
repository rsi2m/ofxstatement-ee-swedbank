#!/usr/bin/python3
"""Setup
"""
from setuptools import find_packages
from distutils.core import setup

version = "0.0.1"

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="ofxstatement-ee-swedbank",
    version=version,
    author="Sergei Mihhailov",
    author_email="me@rsi2m.dev",
    url="https://github.com/rsi2m/ofxstatement-ee-seb",
    description=("Plugin for estonian Swedbank bank"),
    long_description=long_description,
    license="GPLv3",
    keywords=["ofx", "banking", "statement"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["ofxstatement", "ofxstatement.plugins"],
    entry_points={
        "ofxstatement": ["ee-swedbank = ofxstatement.plugins.ee_swedbank:EstoniaSwedbankPlugin"]
    },
    install_requires=["ofxstatement"],
    include_package_data=True,
    zip_safe=True,
)
