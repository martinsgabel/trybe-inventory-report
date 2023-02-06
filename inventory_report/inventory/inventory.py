from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

import csv


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        data = []

        with open(path, mode="r") as file:
            csv_file = csv.DictReader(file)
            for line in csv_file:
                data.append(line)

        if type == "simple":
            SimpleReport.generate(data)

        if type == "completo":
            CompleteReport.generate(data)
