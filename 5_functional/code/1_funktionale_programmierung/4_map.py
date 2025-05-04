"""
Die Funktion `map()` ist eine eingebaute Funktion in Python, mit der
man eine Funktion auf jedes Element eines iterierbaren Objekts anwenden
kann. Dabei entsteht ein Iterator mit den Ergebnissen der Anwendung.

Syntax: map(funktion, iterable)

Oft wird `map()` in Kombination mit `lambda` oder einer definierten
Funktion genutzt, um Transformationen effizient durchzuführen.

Wichtig: Der Rückgabewert von `map()` ist ein Iterator, keine Liste.
Will man das Ergebnis als Liste haben, muss man `list()` verwenden.

Reale Anwendungsbeispiele:
- Umrechnung von Einheiten (z. B. Celsius → Fahrenheit)
- Extraktion oder Transformation von Feldern in Datensätzen
- Normalisierung oder Formatierung von Strings

Dieses Skript zeigt den Einsatz von `map()` in mehreren realistischen
Szenarien.
"""

import timeit

# Quadriere alle Zahlen in einer Liste
numbers = [1, 3, 4]


# Länge jedes Worts in einer Liste berechnen
words = ["the", "brown", "fox", "jumps"]


# Zwei Listen elementweise addieren
def summe(a, b):
    return a + b


lst1 = [2, 4, 6, 8]
lst2 = [1, 3, 5, 7, 9]


# ###########################################
# Drei Listen elementweise multiplizieren
# ###########################################


def multiply(a, b, c):
    return a * b * c


lst3 = [2, 3, 5, 7, 11, 13, 17]
lst2 = [1, 3, 5, 7, 9]
lst1 = [2, 4, 6, 8]

# Alternative mit zip und List Comprehension

# Sinnvolle Anwendung mit map: Summiere zwei Listen elementweise
# über zip() und die eingebaute Funktion sum()
a = [1, 2, 1]
b = [4, 5, -127]


# Aufgabe: erstelle eine Funktion, die als Parameter eine Liste erwartet und
# jeweils den ersten Buchstabens eines Elements in Uppercase wandelt.
# z.b eggs => Eggs spam whomp = Spam Whomp
# Return Liste
monty = ["eggs", "spam whomp", "cheese", "ham"]


# Messung Listen Comprehension vs. map
# List Comprehension ist unter Umständen etwas langsamer
