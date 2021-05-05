import PyYAML
from serializer.objects.base_serializer import *


class YamlSerializer(ISerializer):
    def dumps(self, obj: object) -> str:
        return PyYAML.dumps(obj)

    def loads(self, s: str) -> object:
        return PyYAML.loads(s)
