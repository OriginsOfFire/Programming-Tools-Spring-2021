import inspect
import builtins
from types import CodeType, FunctionType

PRIMITIVES = [int, float, str, bool, list, tuple, type(None)]


def object_to_dict(obj):
    res = {}
    if type(obj) is list:
        counter = 1
        for item in obj:
            res["Variable" + str(counter)] = item
            counter += 1
        return res
    elif type(obj) is dict:
        return obj
    elif type(obj) in PRIMITIVES:
        res["Variable"] = obj
    else:
        res += obj.__dict__
    return res


def dict_to_object(source):
    keys = source.keys()
    if "Variable" in keys:
        return source["Variable"]
    elif "Variable1" in keys:
        res = []
        for key in keys:
            res.append(source[key])
        return res
    elif type(source) is dict:
        return source


def func_to_dict(func):
    members = inspect.getmembers(func.__code__)
    func_dict = {}
    for item in members:
        if item[0].startswith('co'):
            func_dict[item[0]] = item[1]
    func_dict['co_code'] = list(func_dict['co_code'])
    func_dict['co_lnotab'] = list(func_dict["co_lnotab"])

    res = {'code' : func_dict}
    globs = dict()
    name = func['code']['co_name']
    globs[name] = name + '<function>'
    key_values = func.__globals__.items()
    for (key, value) in key_values:
        if value in PRIMITIVES:
            globs[key] = value
    res['globals'] = globs
    return res


def dict_to_function(source):
    globs = source['globals']
    globs['__builtins__'] = builtins
    code_args = source['code']

    res_obj = CodeType(code_args['co_argcount'],
                      code_args['co_posonlyargcount'],
                      code_args['co_kwonlyargcount'],
                      code_args['co_nlocals'],
                      code_args['co_stacksize'],
                      code_args['co_flags'],
                      bytes(code_args['co_code']),
                      tuple(code_args['co_consts']),
                      tuple(code_args['co_names']),
                      tuple(code_args['co_varnames']),
                      code_args['co_filename'],
                      code_args['co_name'],
                      code_args['co_firstlineno'],
                      bytes(code_args['co_lnotab']),
                      tuple(code_args['co_freevars']),
                      tuple(code_args['co_cellvars']))

    temp = FunctionType(res_obj, globs, code_args['co_name'])
    name = code_args['co_name']
    globs[name] = temp
    return FunctionType(res_obj, globs, name)
