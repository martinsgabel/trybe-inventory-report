from inventory_report.importer.importer import Importer

import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        data = []

        try:
            if not path.endswith('.csv'):
                raise ValueError

            with open(path, mode="r") as file:
                csv_file = csv.DictReader(file)
                for line in csv_file:
                    data.append(line)
                return data
        except ValueError:
            raise ValueError("Arquivo inválido")
