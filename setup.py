#!/usr/bin/env python
import sys

from setuptools import setup

PY2 = sys.version_info.major == 2

project = "rdflib-sqlalchemy"
version = "0.4.1.dev0"


setup(
    name=project,
    version=version,
    description="rdflib extension adding SQLAlchemy as an AbstractSQLStore back-end store",
    author="Graham Higgins, Adam Ever-Hadani",
    author_email="gjhiggins@gmail.com, adamhadani@globality.com",
    url="http://github.com/RDFLib/rdflib-sqlalchemy",
    packages=["rdflib_sqlalchemy"],
    download_url="https://github.com/RDFLib/rdflib-sqlalchemy/zipball/master",
    license="BSD",
    platforms=["any"],
    long_description="""
    SQLAlchemy store formula-aware implementation.
    It stores its triples in the following partitions:

    * Asserted non rdf:type statements
    * Asserted rdf:type statements (in a table which models Class membership).
      The motivation for this partition is primarily improved query speed and
      scalability as most graphs will always have more rdf:type statements than
      others.
    * All Quoted statements

    In addition it persists namespace mappings in a separate table
    """,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    install_requires=[
        "alembic>=0.8.8",
        "rdflib>=4.0",
        "six>=1.10.0",
        "SQLAlchemy>=1.1.4",
    ],
    setup_requires=[
        "nose>=1.3.6",
    ],
    tests_require=[
        "coveralls",
        'mock==3.0.5 ; python_version==\"2.7\"',
    ],
    test_suite="nose.collector",
    entry_points={
        'rdf.plugins.store': [
            'SQLAlchemy = rdflib_sqlalchemy.store:SQLAlchemy'
        ]
    }
)
