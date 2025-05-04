"""
Dieses Skript demonstriert eine rekursive Implementierung der
Binärsuche (Binary Search) in Python.

Die Binärsuche ist ein effizientes Verfahren, um ein Element in einer
**sortierten** Liste zu finden. Dabei wird die Liste bei jedem Schritt
halbiert, sodass der Suchbereich logarithmisch schrumpft (O(log n)).

**Voraussetzung:** Die Liste muss aufsteigend sortiert sein.

Vorteile der rekursiven Variante:
- eleganter und kompakter Code
- gut geeignet für bildungsorientierte Zwecke (z. B. Algorithmenlernen)

Nachteile:
- tiefe Rekursion kann bei sehr großen Listen zum Stack Overflow führen

Dieses Skript enthält eine rekursive Funktion zur Binärsuche und ein
Beispiel zur Anwendung.
"""


def binary_search_recursive(arr, target, left=0, right=None):
    pass


# Beispiel
zahlen = [1, 3, 5, 7, 9, 11, 13, 15, 17]
ziel = 7
index = binary_search_recursive(zahlen, ziel)

if index != -1:
    print(f"Zahl {ziel} gefunden an Index {index}.")
else:
    print(f"Zahl {ziel} nicht gefunden.")
