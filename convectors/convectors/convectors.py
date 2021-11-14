import json
from configparser import ConfigParser
from os import path


class Convector:
    """
    ConvectorINI class.
    """

    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file


class ConvectorINI(Convector):
    """
    ConvectorINI class.
    """

    def __init__(self, path_to_file: str):
        super().__init__(path_to_file)

    def dumps(self, indent: int = 2) -> str:
        """
        Convert ini file to json.
        """
        config = ConfigParser()
        config.read(path.abspath(self.path_to_file))

        d = self.to_dict(config)
        return json.dumps(d, indent=indent, ensure_ascii=False)

    @staticmethod
    def to_dict(config: ConfigParser) -> dict:
        """
        Parse config to dict.
        """
        result = {}
        for section_name in config.sections():
            result[section_name] = dict(config[section_name])
        return result
