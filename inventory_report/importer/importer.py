from abc import ABC, abstractmethod

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Importer(ABC):
    @abstractmethod
    def import_data(path: str):
        if "cvs" in path:
            return CsvImporter.import_data(path)
        if "json" in path:
            return JsonImporter.import_data(path)
        if "xml" in path:
            return XmlImporter.import_data(path)
