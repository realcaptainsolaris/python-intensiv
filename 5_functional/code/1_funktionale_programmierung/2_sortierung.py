"""
In Python kann die eingebaute Funktion `sorted()` verwendet werden,
um Listen und andere iterierbare Objekte zu sortieren. Dabei kann man
mit dem Parameter `key` eine Funktion übergeben, die bestimmt, nach
welchem Kriterium sortiert werden soll.

Oft wird dafür eine Lambda-Funktion verwendet, da sie es erlaubt,
einfach und direkt ein Sortierkriterium zu definieren, ohne eine
separate Funktion schreiben zu müssen.

Beispiel:
sorted(liste, key=lambda x: x[1])  # Sortiert nach dem zweiten Element

Python verwendet eine stabile Sortierung. Das bedeutet, dass Elemente
mit gleichem Sortierwert ihre ursprüngliche Reihenfolge beibehalten.
Dies ist nützlich, wenn man mehrfach sortieren möchte – z. B. erst
nach Nachnamen, dann nach Vornamen.

Dieses Skript zeigt, wie man `lambda` mit `sorted()` nutzt und erklärt
anhand von Beispielen, was stabile Sortierung bedeutet.
"""

# unsortierte Liste
liste = [3, 5, 1, 9, 1]


# unsortierte ASCII Buchstaben
chars = ["a", "f", "c", "d", "e"]


# Großbuchstaben kommen vor Kleinbuchsten (A=65, a=97)
chars = ["a", "f", "b", "B", "A", "d", "e", "ü", "u", "z"]


# Sortieren von Strings mit lambda Funktion
chars = ["A", "a", "f", "b", "B", "A", "d", "e"]


# AUFGABE
# Sortiere nach der Zahl
# Ergebnis:
# ids sorted:  ['idx1', 'id2', 'id3', 'id4', 'id5', 'idy5']
ids = ["id5", "idx1", "id2", "idy5", "id4", "id3"]
