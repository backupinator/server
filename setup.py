'''Setup.py'''

from distutils.core import setup
from setuptools import find_packages

setup(
    name='server',
    version='0.0.0',
    author='Nicholas McKibben',
    author_email='nicholas.bgp@gmail.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/backupinator/server',
    license='GPLv3',
    description=('Application running on publicly accessible server '
                 'to coordinate interactions between clients and '
                 'targets.'),
    long_description=open('README.rst').read(),
    install_requires=[
        "flask>=1.1.1",
        "peewee>=3.13.1",
    ],
    python_requires='>=3.6',
)
