from serializer.objects.base_serializer import object_to_dict
from serializer.objects.json_serializer import JsonFactory
from serializer.objects.pickle_serializer import PickleFactory
from serializer.objects.yaml_serializer import YamlFactory
from serializer.objects.toml_serializer import TomlFactory

CUR_PATH = ""
FILE_EXTENSION = ".txt"


class SubObjectParent:
    def __init__(self):
        self.a = 1
        self.b = "2"
        self.c = True


class SubObject(SubObjectParent):
    def __init__(self):
        SubObjectParent.__init__(self)
        self.d = {"a": 13, "top": "kek", "SPAM": "eggs"}


class TestClass():
    num = int
    flt = float
    txt = str
    bul = bool
    arr = list
    tup = tuple
    sed = set
    dct = dict
    obj = object

    def init(self):
        self.num = 42
        self.flt = 3.1416
        self.txt = "Test de test"
        self.bul = True
        self.arr = [13, 69, 420, 0]
        self.dct = {"a": 13, "42": "13", "top": "kek", "meh": ["eggs", "SPAM"]}
        self.obj = SubObject()

    def __str__(self):
        s = ""
        s += type(self).__name__
        s += "\n"
        for (k, v) in object_to_dict(self).items():
            s += f"{k} = {v} \n"
        return s


test_object = TestClass()
test_object.init()


# print(LeObject)


def check_creator(creator):
    s = creator.dumps(test_object)
    obj = creator.loads(s, TestClass)
    assert str(obj) == str(test_object)

    fn = CUR_PATH + type(creator).__name__ + FILE_EXTENSION
    s = creator.dump(test_object, fn)
    obj = creator.load(fn, TestClass)
    assert str(obj) == str(test_object)


def test_json():
    creator = JsonFactory()
    check_creator(creator)


def test_pickle():
    creator = PickleFactory()
    check_creator(creator)


def test_yaml():
    creator = YamlFactory()
    check_creator(creator)


def test_toml():
    creator = TomlFactory()
    check_creator(creator)
