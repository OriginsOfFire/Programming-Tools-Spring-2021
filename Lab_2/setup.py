from setuptools import setup

setup(
    name='wtf_converter',
    version='1.0.0',
    author="yegorique",
    python_requires=">=3.6",
    packages=['parsers.json_parser', 'parsers.toml_parser',
              'parsers.yaml_parser', 'parsers.pickle_parser',
              'parsers.serializer_creator']
)