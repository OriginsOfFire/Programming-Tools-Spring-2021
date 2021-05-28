from object_converter import Converter
import inspect


class BaseSerializer:
    def __init__(self):
        self.__converter = Converter()

    def dumps(self, obj):
        if inspect.isfunction(obj):
            return self.__converter.function_to_dict(obj)
        else:
            return self.__converter.object_to_dict(obj)

    def dump(self, obj, path):
        with open(path, 'w') as file:
            file.write(self.dumps(obj))

    def loads(self, dick):
        if 'code' in dick:
            return self.__converter.dict_to_function(dick)
        else:
            return self.__converter.dict_to_object(dick)

    def load(self, path):
        with open(path, 'r') as file:
            return self.loads(file.read())
