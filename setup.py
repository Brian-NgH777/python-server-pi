from setuptools import setup, find_packages

setup(
    name='pythoncli',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests'
    ],
    version='0.0.1',
    entry_points='''
    [console_scripts]
    pythoncli=pythoncli:pythoncli
    '''
)