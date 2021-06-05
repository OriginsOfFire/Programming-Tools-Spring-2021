from factory.Parser import Parser
from factory.parsers import pickleparser


class PICKLEParser(Parser):
    def dump(self, obj, fp):
        return pickleparser.dump(obj, fp)

    def dumps(self, obj):
        return pickleparser.dumps(obj)

    def load(self, fp):
        return pickleparser.load(fp)

    def loads(self, s):
        return pickleparser.loads(s)
