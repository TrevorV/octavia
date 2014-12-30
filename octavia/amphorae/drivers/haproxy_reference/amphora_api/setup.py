# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='amphora_api',
    version='0.1',
    description='',
    author='',
    author_email='',
    install_requires=[
        "pecan",
        "wsme"
    ],
    test_suite='amphora_api',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup'])
)