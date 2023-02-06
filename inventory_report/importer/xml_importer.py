from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        try:
            with open(path, mode="r") as file:
                xml_file = xmltodict.parse(file.read())
                formated_file = xml_file["dataset"]["record"]
                return formated_file
        except Exception:
            raise ValueError("Arquivo inválido")
