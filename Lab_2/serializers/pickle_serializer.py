import pickle
from .base_serializer import BaseSerializer


class PickleBaseSerializer(BaseSerializer):
    def dumps(self, obj):
        return pickle.dumps(super().dumps(obj))

    def dump(self, obj, path):
        with open(path, 'wb') as file:
            pickle.dump(obj, file)

    def loads(self, string):
        return super().loads(pickle.loads(string))

    def load(self, path):
        with open(path, 'rb') as file:
            return pickle.load(file)
