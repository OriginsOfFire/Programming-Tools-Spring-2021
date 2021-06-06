from factory.JSONParser import JSONParser
from factory.TOMLParser import TOMLParser
from factory.YAMLParser import YAMLParser
from factory.PICKLEParser import PICKLEParser


EXTENSIONS = {
    "JSON": "json",
    "YAML": "yaml",
    "TOML": "toml",
    "PICKLE": "pickle",
}


class Factory(object):
    @staticmethod
    def get_parser(target_format: str):
        ft = target_format.lower()
        if ft == EXTENSIONS["JSON"]:
            return JSONParser()
        elif ft == EXTENSIONS["YAML"]:
            return YAMLParser()
        elif ft == EXTENSIONS["TOML"]:
            return TOMLParser()
        elif ft == EXTENSIONS["PICKLE"]:
            return PICKLEParser()
        else:
            raise ValueError
