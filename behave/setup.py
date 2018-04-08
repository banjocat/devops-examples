from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name='jacks-behave-demo',
    version='0.0.1',
    description='a project',
    packages=find_packages(exclude=[]),
    install_requires=[
        'behave',
        ],
    data_files=[],
    entry_points={
    'console_scripts': []
    },
) 
