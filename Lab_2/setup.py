from setuptools import setup, find_packages

setup(
    name='serializer',
    version='0.42',
    packages=find_packages(),
    description='Custom Python object serializer',
    install_requires=['toml', 'PyYAML'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    scripts=['bin/run.py']
)