from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(self, list_of_dict):
        fab_date = [
            list_of_dict["data_de_fabricacao"] for item in list_of_dict
        ]

        valid_date = [
            list_of_dict["data_de_validade"] for item in list_of_dict
            if list_of_dict["data_de_validade"] > str(date.today())
        ]

        companies = [
            list_of_dict["nome_da_empresa"] for item in list_of_dict
        ]

        company_t = Counter(companies).most_common(1)
        x, y = company_t[0]

        return (
            f"Data de fabricação mais antiga: {min(fab_date)}"
            f"Data de validade mais próxima: {max(valid_date)}"
            f"Empresa com mais produtos: {x}"
        )
