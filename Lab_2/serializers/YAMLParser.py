from factory.Parser import Parser
from factory.parsers import yamlparser


class YAMLParser(Parser):
    def dump(self, obj, fp):
        return yamlparser.dump(obj, fp)

    def dumps(self, obj):
        return yamlparser.dumps(obj)

    def load(self, fp):
        return yamlparser.load(fp)

    def loads(self, s):
        return yamlparser.loads(s)
