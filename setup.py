#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-haystack-panel',
    version='0.1.0',
    description='A Django Debug Toolbar panel for Haystack',
    long_description=open('README.md').read(),
    author='Chris Streeter',
    author_email='chris@chrisstreeter.com',
    url='http://github.com/streeter/django-haystack-panel',
    license=open('LICENSE').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
    ),
)
