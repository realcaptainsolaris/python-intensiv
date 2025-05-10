"""
Die Funktion `reduce()` stammt aus dem Modul `functools` und wird
verwendet, um eine Folge von Werten zu einem einzelnen Ergebnis
zusammenzufassen, indem eine Funktion wiederholt auf jeweils zwei
Elemente angewendet wird.

Syntax: reduce(funktion, sequenz[, startwert])

Typische Anwendungen:
- Aufsummieren oder Multiplizieren von Zahlen
- Finden von Minima oder Maxima
- Verketten von Strings
- Aggregation oder Akkumulation beliebiger Daten

Hinweis:
Ohne Startwert beginnt `reduce()` mit den ersten beiden Elementen.
Mit Startwert wird dieser als Anfangswert verwendet.

Dieses Skript enthält praktische Beispiele für die Nutzung von `reduce()`
in Kombination mit vordefinierten und anonymen Funktionen sowie
Operatoren.
"""

from functools import reduce
import operator as op

# Produkt aller Zahlen in der Liste berechnen
num = [2, 4, 5]
