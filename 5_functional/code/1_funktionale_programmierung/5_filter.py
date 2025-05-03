"""
Die Funktion `filter()` in Python wird verwendet, um Elemente aus einem
iterierbaren Objekt zu filtern, basierend auf einer Funktion, die
wahrheitswertige Rückgaben liefert.

Syntax: filter(funktion, iterable)

Dabei wird jedes Element des iterierbaren Objekts an die Funktion
übergeben. Nur jene Elemente, für die die Funktion `True` zurückgibt,
werden im Ergebnis enthalten sein.

Der Rückgabewert ist ein Iterator. Um die Ergebnisse zu sehen,
muss man ihn z. B. in eine Liste umwandeln.

Typische Einsatzgebiete:
- Herausfiltern ungerader/gerader Zahlen
- Entfernen leerer oder ungültiger Werte
- Prüfung auf Bedingungen in Datenreihen

Vergleich:
filter(predicate, seq) ist äquivalent zu:
[el for el in seq if predicate(el)]

Dieses Skript zeigt grundlegende und praxisnahe Anwendungen von `filter()`.
"""


# Funktion, die prüft, ob eine Zahl größer als 100 ist
def greater_than_100(x) -> bool:
    return x > 100


# Liste mit Zahlen
zahlen = [1, 111, 2, 222, 3, 333]

# Filtere alle Zahlen > 100 mit filter()


# Funktion, die prüft, ob ein Wort länger als 5 Buchstaben ist
def check_length(s):
    return len(s) > 5


# Liste von Wörtern
words = ["apple", "banana", "kiwi", "strawberry", "pear"]

# Filtere Wörter mit mehr als 5 Zeichen mit filter()


# Aufgabe: check_length als Lambda-Funktion umschreiben


# Aufgabe: Gleiche Filterung mit List Comprehension umsetzen
