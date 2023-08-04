from .abcwriter import ABCWriter
import csv


class CSVWriter(ABCWriter):
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

        with open(self.filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)

    def write(self, row: tuple):
        with open(self.filename, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def write_detail(self, row: tuple):
        self.write(row)
