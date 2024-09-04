#!/usr/bin/env python

import os
from pathlib import Path
from setuptools import find_packages, setup


lib_folder = os.path.dirname(os.path.realpath(__file__))
with open(Path(lib_folder) / "requirements.txt") as f:
    requirements = f.read().split()
    pass


setup(
    name="expert_kb",
    version="v0.1.0",
    description="Knowledge base interface for 'expert'",
    author="Liam Tengelis",
    author_email="liam.tengelis@blacktuskdata.com",
    packages=find_packages(),
    package_data={
        "": ["*.yaml"],
        "expert_kb": ["py.typed"],
    },
    install_requires=requirements,
)
