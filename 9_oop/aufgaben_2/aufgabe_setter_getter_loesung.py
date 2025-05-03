"""
Vervollständige die Klasse Produkt und lege die entsprechenden Properties an.

- Der Name muss mindestens drei Zeichen lang sein
- Der Preis darf nicht negativ sein und muss eine Zahl sein
- Die Verfügbarkeit muss den Zustand "in stock" oder "out of stock haben".

Implementiere auch __str__ und __repr__.

"""

class Produkt:
    def __init__(self, name, preis, verfuegbarkeit):
        # Hier müssen die privaten Instanzvariablen initialisiert werden
        self.name = name
        self.preis = preis
        self.verfuegbarkeit = verfuegbarkeit

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) <  3:
            raise ValueError("Ungültiger Produktname")
        self._name = name

    @property
    def preis(self):
        return self._name

    @preis.setter
    def preis(self, preis):
        if not all(
            [isinstance(preis, (float, int)),
            preis >= 0]
        ):
            raise ValueError("Ungültiger Preis")
        self._preis = preis

    @property
    def verfuegbarkeit(self):
        return self._verfuegbarkeit

    @verfuegbarkeit.setter
    def verfuegbarkeit(self, verfuegbarkeit):
        if verfuegbarkeit not in ["in stock", "out of stock"]:
            raise ValueError("Ungültige verfuegbarkeit")
        self._verfuegbarkeit = verfuegbarkeit

    def __str__(self) -> str:
        return self.name

products = [
    ("Maggi", 23.2, "in stock"),
    ("Snickers", 4, "out of stock"),
    ("Petersilie", 1.9, "stock"),  # muss scheitern
    ("Gouda Käse", -12.50, "out of stock"), # muss scheitern
    ("Za", 23.2, "in stock"),  # muss scheitern.
]

def test(products):
    for product in products:
        try:
            p = Produkt(*product)
        except ValueError as e:
            print(e, product)
        else:
            print(f"{p} ist ein gültiges Produkt.")


if __name__ == "__main__":
    test(products)
