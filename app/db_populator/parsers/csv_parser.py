import csv
from .file_parser import FileParser


class CSVFileParser(FileParser):

    def parse(self, file_path):
        result = []
        with open(file=file_path, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                result.append(row)
        return result
