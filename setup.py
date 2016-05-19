# -*- coding:utf-8 -*-

from setuptools import setup

setup(
    name='matterweb',
    version="1.0.0",
    description="mattermost for incomming webhook",
    author="BaobabDuncan",
    author_email="baobab.duncan@gmail.com",
    license="MIT License",
    url="",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4"
    ],
    install_requires=["requests"],
    packages=['matterweb'],
    # py_modules=["matterweb"]
)
