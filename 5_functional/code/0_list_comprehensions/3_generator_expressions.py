"""
Generator Expressions ähneln List Comprehensions, erzeugen aber keine
vollständige Liste im Speicher. Stattdessen geben sie einen Iterator
zurück, der die Werte bei Bedarf (lazy evaluation) erzeugt.

Ein Iterator ist ein Objekt, das mit der Funktion `next()` den nächsten
Wert liefert. Sobald alle Werte verbraucht sind, ist der Iterator
erschöpft. Generatoren sind besonders speichereffizient bei großen
Datenmengen, da sie nicht alles auf einmal im Speicher halten.

In diesem Skript zeigen wir den Unterschied zwischen Generator Expressions
und List Comprehensions, insbesondere beim Speicherverbrauch.
"""

import sys

# List Comprehension: Erzeugt sofort eine komplette Liste im Speicher
liste = [x**2 for x in range(1000)]

# Generator Expression: Erzeugt Werte bei Bedarf (lazy evaluation)

# Zugriff auf Elemente im Generator mit next()

# Der Generator ist ein Iterator – er verbraucht sich mit jedem Aufruf
# Wenn man ihn durchläuft, sind die Werte danach weg


# Aufgabe: Schreibe eine Funktion, die einen Generator zurückgibt,
# der nur gerade Zahlen bis zu einem gegebenen Maximum liefert

# Hinweis: Generator Expressions können direkt in Schleifen und
# Funktionen wie sum(), max(), etc. verwendet werden:
