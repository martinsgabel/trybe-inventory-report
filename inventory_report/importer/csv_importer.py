from inventory_report.importer.importer import Importer
from abc import abstractmethod

import csv


class CsvImporter(Importer):
    @abstractmethod
    def import_data(path: str):
        data = []

        try:
            with open(path, mode="r") as file:
                csv_file = csv.DictReader(file)
                for line in csv_file:
                    data.append(line)
                return data
        except ValueError:
            raise ValueError("Arquivo inválido")
