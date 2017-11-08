"""Setup.py config."""
from setuptools import setup

setup(
    name='code_katas',
    description='Various katas from codewars',
    author='Nathan Moore',
    author_email='ncmoore1986@gmail.com',
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'tox'],
        'development': ['ipython']
    },
)
