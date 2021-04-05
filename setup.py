# -*- coding: utf-8 -*-
"""
    setup
    ~~~~
    Flask-SQL-XSS-Injection-check is a simple extension to Flask allowing you to support SQL &
    XSS Injection check.
"""

from setuptools import setup
from os.path import join, dirname

with open(join(dirname(__file__), 'flask_sql_xss_injection_check/version.py'), 'r') as f:
    exec(f.read())

with open (join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(
    name='Flask-SQL-XSS-Injection-Check',
    version=__version__,
    url='',
    license='MIT',
    author='Deepak Singh',
    author_email='',
    description="A Flask extension for SQL XSS Injection check support",
    packages=['flask_sql_xss_injection_check'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    tests_require=[
        'nose',
        'packaging'
    ],
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)