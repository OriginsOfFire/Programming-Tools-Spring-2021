import inspect
import types
import re

CLASS_TYPE_REGEX = "\'([\w\W]+)\'"
FUNC = "function"
FUNC_ATTR = [ "__code__", "__name__", "__defaults__", "__closure__"]
CODE_FIELD = "__code__"
TYPE_FIELD = "TYPE"
VALUE_FIELD = "VALUE"
GLOBS = "__globals__"
GLOBAL_FIELDS = 'co_names'
CODE_ARGS = (
    'co_argcount',
    'co_posonlyargcount',
    'co_kwonlyargcount',
    'co_nlocals',
    'co_stacksize',
    'co_flags',
    'co_code',
    'co_consts',
    'co_names',
    'co_varnames',
    'co_filename',
    'co_name',
    'co_firstlineno',
    'co_lnotab',
    'co_freevars',
    'co_cellvars'
)


def serialize_obj(obj):
    res = dict()
    tp = type(obj)
    type_string = re.search(CLASS_TYPE_REGEX, str(tp)).group(1)

    if tp == bytes:
        res[TYPE_FIELD] = type_string
        res[VALUE_FIELD] = list(obj)
    elif tp == dict:
        for name, value in obj.items():
            res[name] = serialize_obj(value)
    elif tp == list or tp == tuple:
        res[TYPE_FIELD] = type_string
        res[VALUE_FIELD] = list()
        for value in obj:
            res[VALUE_FIELD].append(serialize_obj(value))
    elif isinstance(obj, (int, float, complex, bool, str)) or obj is None:
        return obj
    elif inspect.isroutine(obj):
        res[TYPE_FIELD] = type_string
        res[VALUE_FIELD] = serialize_func(obj)
    else:
        res[TYPE_FIELD] = type_string
        res[VALUE_FIELD] = serialize_instance(obj)
    return res


def serialize_func(func):
    res = {}
    members = inspect.getmembers(func)
    for member in members:
        if inspect.isbuiltin(member[1]):
            continue
        if member[0] in FUNC_ATTR:
            res[member[0]] = serialize_obj(member[1])
            if member[0] == CODE_FIELD:
                res[GLOBS] = {}
                globs = func.__getattribute__(GLOBS)
                for name in member[1].__getattribute__(GLOBAL_FIELDS):
                    if name == func.__name__:
                        res[GLOBS][name] = func.__name__
                        continue
                    if name in __builtins__:
                        continue
                    if name in  globs:
                        if inspect.ismodule(globs[name]):
                            continue
                        res[GLOBS][name] = serialize_obj(globs[name])
    return res


def serialize_instance(instance):
    res = dict()
    attributes = inspect.getmembers(instance)
    for attr in attributes:
        if callable(attr[1]):
            continue
        res[attr[0]] = serialize_obj(attr[1])
    return res
