import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        try:
            with open(path, mode="r") as file:
                json_file = json.load(file)
                return json_file
        except json.JSONDecodeError:
            raise ValueError("Arquivo inválido")
