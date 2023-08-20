import json
from .file_parser import FileParser


class JSONFileParser(FileParser):
    def parse(self, file_path):
        result = None
        with open(file=file_path, mode='r') as f:
            result = json.load(f)
        return result
