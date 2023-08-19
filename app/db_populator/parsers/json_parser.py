import json
from .file_parser import FileParser


class JSONFileParser(FileParser):
    def parse(self, file_path):
        parsed_file = None
        with open(file=file_path, mode='r') as f:
            parsed_file = json.load(f)
        return parsed_file
