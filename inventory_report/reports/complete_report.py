from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data: list):
        list_of_companies_qtd = ""

        simple_report = SimpleReport.generate(data) + "\n"

        counter = Counter(item["nome_da_empresa"] for item in data)

        for item in counter.items():
            x, y = item
            list_of_companies_qtd += f"- {x}: {y}\n"

        return (
            simple_report
            + "Produtos estocados por empresa:\n"
            + list_of_companies_qtd
        )
