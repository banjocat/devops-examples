from setuptools import setup, find_packages

setup(
    name='jacks-click-demon',
    version='0.0.1',
    description='a project',
    packages=find_packages(exclude=[]).append('main'),
    install_requires=[
        'click'
        ],
    data_files=[],
    entry_points={
        'console_scripts': []
    },
)
