import json
from .base_serializer import BaseSerializer


class JsonBaseSerializer(BaseSerializer):
    def dumps(self, obj):
        return json.dumps(super().dumps(obj), indent=4)

    def dump(self, obj, path):
        with open(path, 'w') as file:
            json.dump(obj, file)

    def loads(self, string):
        return super().loads(json.loads(string))

    def load(self, path):
        with open(path, 'r') as file:
            return json.load(file)
