"""
Dict Comprehensions sind ähnlich wie List Comprehensions, aber sie
werden verwendet, um Dictionaries auf elegante und kompakte Weise zu
erstellen. Dabei werden Schlüssel-Wert-Paare direkt erzeugt.

Dieses Skript zeigt grundlegende Anwendungen von Dict Comprehensions.
"""

# Klassisches Erstellen eines Dictionaries mit einer Schleife
quadrate = {}
for i in range(6):
    quadrate[i] = i**2
print(quadrate)


# Das gleiche Dictionary mit einer Dict Comprehension erzeugen


# Dict Comprehension mit Bedingung: Nur ungerade Zahlen berücksichtigen


# Strings als Schlüssel: Wörter und ihre Längen
woerter = ["Apfel", "Banane", "Kiwi"]


# Umkehrung eines Dictionaries: Schlüssel und Werte tauschen
original = {"a": 1, "b": 2, "c": 3}


# Aufgabe: Erzeuge ein Dictionary aus einer Liste von Zahlen,
# wobei jede Zahl der Schlüssel ist und ihr Quadrat der Wert.
zahlen = [1, 2, 3, 4, 5]


# Aufgabe: Verdoppele alle Werte in einem gegebenen Dictionary
preise = {"Apfel": 1.0, "Banane": 0.5, "Kiwi": 1.5}
