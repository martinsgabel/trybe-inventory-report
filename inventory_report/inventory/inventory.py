from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        data = []

        # try:
        #     ....
        # except:
        #     ...
        #     try:
        #         ....
        #     except:
        #         ... try:

        try:
            data = Inventory.sort_format(path)
        except ValueError:
            raise ValueError("Arquivo inválido")

        if type == "simples":
            return SimpleReport.generate(data)

        if type == "completo":
            return CompleteReport.generate(data)

    @staticmethod
    def sort_format(path):
        if "csv" in path:
            return CsvImporter.import_data(path)
        if "json" in path:
            return JsonImporter.import_data(path)
        if "xml" in path:
            return XmlImporter.import_data(path)
