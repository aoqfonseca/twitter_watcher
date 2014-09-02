# -*- coding: utf-8 -*-
# The MIT License (MIT)
# Copyright (c) 2014 Andre Fonseca
import codecs

from setuptools import setup, find_packages
from twitter_watcher import __version__

README = codecs.open('README.markdown', encoding='utf-8').read()

setup(
    name="twitter-watcher",
    version=__version__,
    description="Frontend as-a-service API for Twitter Stream Client",
    long_description=README,
    author="Andre Fonseca",
    author_email="aoqfonseca@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages(exclude=["docs", "tests", "samples"]),
    include_package_data=True,
    install_requires=["Flask==0.9",
                      "jsonschema",
                      "mongoengine",
                      "requests",
                      "flask-script",
                      "arrow",
                      "flask-mongoengine"]
)
