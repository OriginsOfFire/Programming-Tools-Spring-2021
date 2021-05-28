import inspect
import builtins
from types import CodeType, FunctionType
from collections import namedtuple


class Converter:
    @staticmethod
    def __is_primitive(obj):
        return type(obj) in [int, float, bool, str, type(None)]

    def __dict_converter(self, obj):
        res = {}
        for key, value in obj.items():
            if self.__is_primitive(value):
                res[key] = value
            else:
                res[key] = self.object_to_dict(value)
        return res

    def object_to_dict(self, obj):
        res = {}
        if self.__is_primitive(obj):
            return obj
        elif isinstance(obj, list):
            res = list()
            for item in obj:
                res.append(self.object_to_dict(item))
            return res
        elif isinstance(obj, dict):
            return self.__dict_converter(obj)
        else:
            return self.__dict_converter(obj.__dict__)

    def dict_to_object(self, dick):
        if self.__is_primitive(dick):
            return dick
        elif isinstance(dick, list):
            res = []
            for item in dick:
                res.append(self.dict_to_object(item))
            return res

        else:
            res = {}
            for key, value in dick.items():
                if not self.__is_primitive(value):
                    res[key] = self.dict_to_object(value)
                else:
                    res[key] = value
            return namedtuple('object', res.keys())(*res.values())

    def function_to_dict(self, func):
        res, code = {}, {}
        code_pairs = inspect.getmembers(func.__code__)
        for key, value in code_pairs:
            if str(key).startswith('co_'):
                if isinstance(value, bytes):
                    value = (list(value))
                code[key] = value
        res['code'] = code

        globs = {}
        name = res['code']['co_name']
        globs[name] = name + '<function>'
        global_pairs = func.__globals__.items()
        for key, value in global_pairs:
            if self.__is_primitive(value):
                globs[key] = value
        res['globals'] = globs
        return res

    def dict_to_function(self, dick):
        globs = dick['globals']
        globs['__builtins__'] = builtins
        args = dick['code']

        code = CodeType(args['co_argcount'],
                                 args['co_posonlyargcount'],
                                 args['co_kwonlyargcount'],
                                 args['co_nlocals'],
                                 args['co_stacksize'],
                                 args['co_flags'],
                                 bytes(args['co_code']),
                                 tuple(args['co_consts']),
                                 tuple(args['co_names']),
                                 tuple(args['co_varnames']),
                                 args['co_filename'],
                                 args['co_name'],
                                 args['co_firstlineno'],
                                 bytes(args['co_lnotab']),
                                 tuple(args['co_freevars']),
                                 tuple(args['co_cellvars']))
        temp = FunctionType(code, globs, args['co_name'])
        name = args['co_name']
        return FunctionType(code, globs, name)