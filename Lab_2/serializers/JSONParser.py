from factory.Parser import Parser
from factory.parsers import jsonparser


class JSONParser(Parser):
    def dump(self, obj, fp):
        return jsonparser.dump(obj, fp)

    def dumps(self, obj):
        return jsonparser.dumps(obj)

    def load(self, fp):
        return jsonparser.load(fp)

    def loads(self, s):
        return jsonparser.loads(s)
