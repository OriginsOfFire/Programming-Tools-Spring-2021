from factory.Parser import Parser
from factory.parsers import tomlparser


class TOMLParser(Parser):
    def dump(self, obj, fp):
        return tomlparser.dump(obj, fp)

    def dumps(self, obj):
        return tomlparser.dumps(obj)

    def load(self, fp):
        return tomlparser.load(fp)

    def loads(self, s):
        return tomlparser.loads(s)
