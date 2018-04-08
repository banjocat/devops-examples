from setuptools import setup, find_packages

setup(
    name='test-demo',
    version='0.0.1',
    description='a project',
    packages=find_packages(exclude=[]),
    install_requires=[
        'behave',
        # 'sarge'
        ],
    data_files=[],
    entry_points={
    'console_scripts': []
    },
) 
