#! /usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='aiosteamworksweb',
    version=None,  # TODO
    author='insurgency.gg',
    url='https://github.com/insurgency/aiosteamworksweb',
    packages=find_packages(
        exclude=[
            'tests',
        ],
    ),
    classifiers=[
    ],
    license='MIT',
    python_requires='>=3.8',
    test_suite='tests',
    install_requires=[
        'aiohttp >= 3.6.1',
    ],
)
