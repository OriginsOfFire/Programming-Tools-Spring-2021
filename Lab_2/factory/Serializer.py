from factory.parsers.serializer import serialize_obj, deserialize_obj


class Serializer:
    def serialize_obj(self, obj: object):
        return serialize_obj(obj)

    def deserialize_obj(self, obj: dict):
        return deserialize_obj(obj)
