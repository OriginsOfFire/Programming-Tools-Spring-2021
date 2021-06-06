from setuptools import setup
from setuptools import find_packages

setup(
    name='consoleserializer',
    packages=[
        'factory',
        'factory/parsers'
    ],
    version='0.1.7.2',
    description='Console serializer utility',
    author='yegorrique',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='/tests',
    scripts=['bin/consoleserialize']
)