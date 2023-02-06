from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list_of_dict: list):
        fab_date = [
            item["data_de_fabricacao"] for item in list_of_dict
        ]

        valid_date = [
            item["data_de_validade"] for item in list_of_dict
            if item["data_de_validade"] > str(date.today())
        ]

        companies = [
            item["nome_da_empresa"] for item in list_of_dict
        ]

        company_t = Counter(companies).most_common(1)

        return (
            f"Data de fabricação mais antiga: {min(fab_date)}\n"
            f"Data de validade mais próxima: {min(valid_date)}\n"
            f"Empresa com mais produtos: {company_t[0][0]}"
        )
