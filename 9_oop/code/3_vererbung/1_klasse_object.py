"""
Die Klasse `object` ist die Basisklasse aller Klassen in Python.
Jede Klasse, die du definierst, erbt automatisch von `object`,
auch wenn du es nicht explizit angibst.

Sie bietet grundlegende Methoden wie:
- __init__(), __str__(), __eq__(), __repr__(), usw.

Diese Datei demonstriert den Zusammenhang mit `object`
und zeigt, wie eigene Klassen davon profitieren.
"""


# Wir definieren eine einfache Klasse ohne explizite Vererbung
# Trotzdem erbt sie automatisch von `object`
class SimpleClass:
    pass


# Wir prüfen, ob SimpleClass von object erbt, mit isinstance()
instance = SimpleClass()
print(isinstance(instance, object))  # Ausgabe: True


# Wir definieren eine Klasse und überschreiben die Methode __str__
# Diese Methode ist in object definiert, daher können wir sie anpassen
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person mit Namen: {self.name}"


# Wir erstellen ein Objekt der Klasse Person und geben es aus
p = Person("Anna")
print(p)  # Ausgabe durch __str__: Person mit Namen: Anna


# Die Methode __eq__ kommt auch von object
# Wir können sie überschreiben, um Gleichheit zu definieren
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Wir vergleichen zwei Objekte der Klasse Point
p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True, da __eq__ überschrieben wurde


# Mit der Funktion dir() kann man sehen, welche Methoden von object
# geerbt wurden. Das geht mit jeder Instanz.
print(dir(b1))
