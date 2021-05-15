from serializer.objects import base_serializer
from serializer.objects import json_serializer
from serializer.objects import pickle_serializer
from serializer.objects import toml_serializer
from serializer.objects import yaml_serializer


def get_creator(extension: str) -> base_serializer.SerializerFactory:
    if extension == 'json':
        return json_serializer.JsonFactory()
    if extension == 'pickle':
        return pickle_serializer.PickleFactory()
    if extension == 'toml':
        return toml_serializer.TomlFactory()
    if extension == 'yaml':
        return yaml_serializer.YamlFactory()
    raise ValueError('Unknown extension: ' + extension)
