import toml
from base_serializer import BaseSerializer


class TomlSerializer(BaseSerializer):
    def dumps(self, obj):
        return toml.dumps(super().dumps(obj))

    def dump(self, obj, path):
        with open(path, 'w') as file:
            toml.dump(file, obj)

    def loads(self, string):
        return super().loads(toml.loads(string))

    def load(self, path):
        with open(path, 'r') as file:
            return toml.load(file)
