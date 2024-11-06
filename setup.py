# -*- coding: utf-8 -*-
from setuptools import setup, find_packages  # noqa: H301

version = {}
with open("iot_api_client/__init__.py") as fp:
    exec(fp.read(), version)

with open("README.md") as f:
    long_description = f.read()

NAME = "arduino-iot-client"
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=version["__version__"],
    description="Iot API",
    author_email="",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Iot API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
