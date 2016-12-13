"""Setupup.py for data-structures repo."""

from setuptools import setup

setup(
    name="data_structure",
    description="Implementation of singly linked list.",
    version=0.1,
    author="Marc Fieser and Rick Valenzuela",
    author_email="midfies@gmail.com",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=['data_structure'],
    install_requires=['ipython'],
    extras_require={
        "test": ['tox', 'pytest', 'pytest-watch', 'pytest-cov']
    },
)
