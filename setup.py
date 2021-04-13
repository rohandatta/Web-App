# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Heart Disease Prediction',
    version='0.1.0',
    description='A web app to predict heart disease based on user information',
    long_description=readme,
    author='Rohan Datta',
    author_email='dattarohan4@gmail.com',
    url='https://github.com/rohandatta/Web-App',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

