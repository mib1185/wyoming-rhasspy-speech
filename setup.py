#!/usr/bin/env python3
from pathlib import Path

import setuptools
from setuptools import setup

this_dir = Path(__file__).parent

requirements = []
requirements_path = this_dir / "requirements.txt"
if requirements_path.is_file():
    with open(requirements_path, "r", encoding="utf-8") as requirements_file:
        requirements = requirements_file.read().splitlines()

module = "wyoming_rhasspy_speech"
module_dir = this_dir / module

data_files = list((module_dir / "templates").rglob("*")) + list(
    (module_dir / "static").rglob("*")
)

# -----------------------------------------------------------------------------


setup(
    name=module,
    version="1.0.0",
    description="Wyoming Server for Rhasspy Speech-to-text",
    url="http://github.com/rhasspy/wyoming-rhasspy-speech",
    author="Michael Hansen",
    author_email="mike@rhasspy.org",
    license="MIT",
    packages=setuptools.find_packages(),
    package_data={module: [str(p.relative_to(module_dir)) for p in data_files]},
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="rhasspy wyoming stt",
)
