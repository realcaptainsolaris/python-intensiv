"""
Aufgabe:
In dieser Aufgabe soll eine sehr große Log-Datei zeilenweise verarbeitet werden,
ohne sie vollständig in den Speicher zu laden.

Schreibe eine Generatorfunktion `read_lines(filename, chunk_size=3)`,
die jeweils `chunk_size` Zeilen auf einmal liefert (mit `yield`).

Ziel:
- Datei zeilenweise einlesen (streamingbasiert)
- Immer nur kleine Portionen (Chunks) in den Speicher laden
- Die Funktion soll sich wie ein Datenstrom verhalten

Beispiel:
Angenommen, die Datei `data.txt` enthält:
Zeile 1
Zeile 2
Zeile 3
Zeile 4
Zeile 5
Zeile 6

Dann soll die Ausgabe lauten:
Chunk gelesen: ['Zeile 1', 'Zeile 2', 'Zeile 3']
Chunk gelesen: ['Zeile 4', 'Zeile 5', 'Zeile 6']
"""
