from inventory_report.importer.importer import Importer
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        data = []

        data = Importer.import_data(path)

        if type == "simple":
            SimpleReport.generate(data)

        if type == "completo":
            CompleteReport.generate(data)
