#!/usr/bin/env python
from setuptools import setup

setup(
    name='amocrm_api',
    version='0.0.1',
    packages=['amocrm'],
    url='https://github.com/Krukov/amocrm_api',
    license='MIT license',
    author='Dmitry Krukov',
    author_email='frog-king69@yandex.ru',
    description='Python (Django like) API for Amocrm',
    long_description=open('README.md').read(),

    requires=[
        'requests (>=2.3)',
        'responses (>=0.2.2)',
    ],
    install_requires=[
        'requests >=2.3',
        'responses >=0.2.2',
    ]
)