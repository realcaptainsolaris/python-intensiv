"""
Funktionen mit `yield` sind sogenannte Generatorfunktionen.
Statt mit `return` einen Wert zurückzugeben und zu beenden, liefern
sie mit `yield` einen Wert und pausieren ihren Zustand – beim nächsten
Aufruf wird der Code direkt nach dem `yield` fortgesetzt.

Generatorfunktionen erzeugen automatisch einen Iterator und sind
speichereffizient, da sie Werte bei Bedarf liefern (Lazy Evaluation).

Typische Anwendungen:
- Große Datenmengen sequentiell verarbeiten
- Unendliche Sequenzen generieren
- Zustandsbehaftete Abläufe abbilden

Dieses Skript zeigt verschiedene Anwendungsbeispiele für `yield`.
"""

# Beispiel 1: Generatorfunktion zur Erzeugung einer Zahlenfolge


def zahlen_bis(max_wert):
    for i in range(max_wert):
        yield i


for zahl in zahlen_bis(5):
    print(zahl)  # Ausgabe: 0 bis 4


# Beispiel 2: Generator, der nur gerade Zahlen liefert
def gerade_zahlen_bis(max_wert):
    for i in range(max_wert):
        if i % 2 == 0:
            yield i


print(list(gerade_zahlen_bis(10)))  # [0, 2, 4, 6, 8]


# Beispiel 3: Unendlicher Generator (z. B. für Streams oder IDs)
def endlose_nummerierung():
    i = 1
    while True:
        yield i
        i += 1


# Achtung: Muss begrenzt werden!
gen = endlose_nummerierung()
for _ in range(5):
    print(next(gen))  # 1 bis 5


# Beispiel 4: Zeilenweises Lesen einer Datei mit `yield`
def datei_zeilenweise_lesen(pfad):
    with open(pfad, "r") as f:
        for zeile in f:
            yield zeile.strip()


# Beispielnutzung (Pfad ggf. anpassen)
# for zeile in datei_zeilenweise_lesen("beispiel.txt"):
#     print(zeile)


# Aufgabe: Generator, der die Quadrate aller Zahlen bis n liefert
def quadrate_bis(n):
    for i in range(n + 1):
        yield i * i


print(list(quadrate_bis(5)))  # [0, 1, 4, 9, 16, 25]
