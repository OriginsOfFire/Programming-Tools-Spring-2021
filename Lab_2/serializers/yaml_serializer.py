from .base_serializer import BaseSerializer
import yaml


class YamlSerializer(BaseSerializer):
    def dumps(self, obj):
        return yaml.dump(super().dumps(obj))

    def dump(self, obj, path):
        with open(path, 'w') as file:
            yaml.dump(obj, file)

    def loads(self, string):
        return super().loads(yaml.load(string))

    def load(self, path):
        with open(path, 'r') as file:
            return yaml.load(file)
