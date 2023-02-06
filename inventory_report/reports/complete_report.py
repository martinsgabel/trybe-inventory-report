from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data: list):
        list_of_companies_qtd = ""

        simple_report = SimpleReport.generate(list)

        counter = Counter(data["nome_da_empresa"] for item in data)

        for item in counter:
            x, y = item
            list_of_companies_qtd = f"- {x}: {y}\n"

        return (
            simple_report
            + "Produtos estocados por empresa:"
            + list_of_companies_qtd
        )
