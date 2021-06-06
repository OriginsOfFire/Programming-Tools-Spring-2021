from factory.parsers import jsonparser
from factory.parsers import tomlparser
from factory.parsers import yamlparser
from factory.parsers import pickleparser
from factory.parsers import serializer
from tests.test_funcs import test_fib, test_func_2, test_another_func


def test_recursive():
    jsonparser.dump(serializer.serialize_obj(test_fib), "tests/test.json")
    temp = serializer.deserialize_obj(jsonparser.load("tests/test.json"))
    assert temp(10) == test_fib(10)


def test_simple():
    tomlparser.dump(serializer.serialize_obj(test_func_2), "tests/test.toml")
    temp = serializer.deserialize_obj(tomlparser.load("tests/test.toml"))
    assert temp(18) == test_func_2(18)


def test_lambda_():
    k = lambda x, y: x**y
    yamlparser.dump(serializer.serialize_obj(k), "tests/test.yaml")
    temp = serializer.deserialize_obj(yamlparser.load("tests/test.yaml"))
    assert k(5, 5) == temp(5, 5)


def test_onemoretest():
    pickleparser.dump(serializer.serialize_obj(test_another_func), "tests/test.pickle")
    temp = serializer.deserialize_obj(pickleparser.load("tests/test.pickle"))
    assert test_another_func(10) == temp(10)


def test_dictjsontest():
    a = dict()
    b = dict()
    c = dict()
    a['a1'] = 15
    a['a2'] = 15.99
    a['a3'] = None
    a['a4'] = 'hello, its me from A'
    b['b1'] = 15
    b['b2'] = 15.99
    b['b3'] = None
    b['b4'] = 'hello, its me from A'
    c['c1'] = 15
    c['c2'] = 15.99
    c['c3'] = None
    c['c4'] = 'hello, its me from A'
    a['a5'] = [[b, c], b, c]
    a['a6'] = True
    a['a7'] = False
    a['a8'] = 'hello, its me from A'
    a['a9'] = 15.99
    a['a10'] = 15
    a['a11'] = None

    jsonparser.dump(a, 'tests/test_dictionary.json')
    k = jsonparser.load('tests/test_dictionary.json')
    assert a == k


def test_dictyamltest():
    a = dict()
    b = dict()
    c = dict()
    a['a1'] = 15
    a['a2'] = 15.99
    a['bruh'] = b
    a['a3'] = None
    a['a4'] = 'hello, its me from A'
    a['a6'] = True
    a['bleh'] = c
    a['good_job'] = list()
    a['a7'] = False
    a['a8'] = [18, -81.99, 'fffhhr', 'rhrhr\tjwdew']
    b['b6'] = 'tratatatata'

    yamlparser.dump(a, 'tests/test_dictionary.yaml')
    k = yamlparser.load('tests/test_dictionary.yaml')
    assert a == k


def test_dicttomltest():
    a = dict()
    b = dict()
    c = dict()
    a['a1'] = 15
    a['a2'] = 15.99
    a['a3'] = b
    a['a4'] = 'hello, its me from A'
    a['a5'] = [[15, 'hello'], [None, True], [-17, 299], False]
    a['a6'] = True
    a['a7'] = False
    b['b6'] = 'tratatatata'
    b['b7'] = c
    c['c1'] = 15
    c['c2'] = 'oraoraoraora'

    tomlparser.dump(a, 'tests/test_dictionary.toml')
    k = tomlparser.load('tests/test_dictionary.toml')
    assert a == k


def test_serialize():
    temp = serializer.serialize_obj(test_fib)
    temp_2 = serializer.deserialize_obj(temp)

    assert temp_2(10) == test_fib(10)
