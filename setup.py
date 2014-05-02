#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import simple_bugs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#version = simple_bugs.__version__
version = '0.1.2'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django_simple_bugs',
    version=version,
    description="""Bug tracking and project management app.""",
    long_description=readme + '\n\n' + history,
    author='Thomas Cabral',
    author_email='thethc3@gmail.com',
    url='https://github.com/thethc3/django_simple_bugs',
    packages=[
        'simple_bugs',
    ],
    include_package_data=True,
    install_requires=[
	'django>=1.5.1',
	'south>=0.8.4',
	'django_haystack>=2.1.0',
	'django_crispy_forms>=1.4.0',
	'django_wysiwyg>=0.5.1',
	'django_simple_history>=1.3.0',
	'djangorestframework>=2.3.12',
    ],
    license="MIT",
    zip_safe=False,
    keywords='django_simple_bugs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)