import pathlib
import abc
import json

BASE_DIR = pathlib.Path(__file__).parent


class JsonExporterValidationError(Exception):
    pass


class ExporterMeta(type):
    subclass_filenames = set()

    def __new__(cls, classname, bases, namespace):
        # cls= ExporterMeta
        print(f"{cls=}")
        print(f"{classname=}")
        print(f"{bases=}")
        print(f"{namespace=}")

        if classname == "JsonExporter":
            return super().__new__(cls, classname, bases, namespace)

        if "_filename" not in namespace:
            raise JsonExporterValidationError(
                "You have to implement _filename in subclass"
            )

        if not isinstance(namespace["_filename"], str):
            raise JsonExporterValidationError("Filename must be a string")

        if not namespace["_filename"].endswith(".json"):
            raise JsonExporterValidationError(
                "Json Files need the Suffix .json")

        if (fn := namespace["_filename"]) in cls.subclass_filenames:
            raise JsonExporterValidationError(
                f"filename {fn} is already in use of another subclass"
            )
        cls.subclass_filenames.add(namespace["_filename"])
        class_new = super().__new__(cls, classname, bases, namespace)
        return class_new


class JsonExporter(metaclass=ExporterMeta):
    def __init__(self, raw_data_list):
        self.raw_data = raw_data_list

    def export(self):
        with open(BASE_DIR / self._filename, "w") as f:
            data = self._build_from_raw_data()
            json.dump(data, f)

    def _build_from_raw_data(self):
        pass


class InvoicesExporter(JsonExporter):
    """
    you need to implement
    _filename
    _build from raw data
    """

    _filename = "invoices.json"

    def _build_from_raw_data(self) -> dict:
        d = []
        for entry in self.raw_data:
            uuid, price = entry
            d.append({"uuid": uuid, "price": price})
        return d


i = InvoicesExporter(
    [
        ["2343XE242343", 50],
        ["234X233222", 100],
        ["234299P999", 120],
        ["AC4233222", 800],
    ]
)
i.export()


class GrumpyInvoicesExporter(JsonExporter):
    _filename = "invoices.json"

    def _build_from_raw_data(self) -> dict:
        """Delete GRUMP prefix"""
        d = []
        for entry in self.raw_data:
            uuid, price = entry
            d.append({"uuid": uuid.split("-")[1], "price": price})
        return d


i = GrumpyInvoicesExporter(
    [
        ["GRUMP-234343", 50],
        ["GRUMP-2342", 100],
        ["GRUMP-231111P999", 120],
        ["GRUMP-XXXXAC4233222", 800],
    ]
)
result = i.export()
print(result)
