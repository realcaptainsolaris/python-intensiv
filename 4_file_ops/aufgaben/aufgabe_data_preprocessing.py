"""
Aufgabe:
In einer CSV-Datei `raw_data.csv` liegen unsaubere Sensordaten:
- Einige Zeilen enthalten fehlende Werte.
- Manche Zahlen sind als Strings mit Komma statt Punkt gespeichert.
- Spaltennamen sind unsauber (z. B. Leerzeichen oder Großbuchstaben).

Beispielinhalt:
Sensor ID , Temperature , Status
S1, 20,OK
S2, ,OK
S3, 19.2,FAIL
S4, "21,5",OK
, 22,OK

Ziel:
Bereinige die Datei schrittweise mit dem Modul `csv`,
sodass ein sauberes CSV entsteht, das dann mit pandas weiterverarbeitet werden könnte.

Vorgaben:
1. Ignoriere Zeilen, in denen Sensor ID oder Temperature fehlt.
2. Ersetze Kommas in Temperaturwerten durch Punkte und konvertiere sie in Float.
3. Vereinheitliche Spaltennamen: Kleinbuchstaben, ohne Leerzeichen.
4. Speichere das Ergebnis in `clean_data.csv`.

Beispielausgabe (clean_data.csv):
sensor_id,temperature,status
S1,20.0,OK
S3,19.0,FAIL
S4,21.5,OK

Hinweis:
Verwende kein pandas für diesen Schritt – nur csv.DictReader / DictWriter.
"""

import csv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "raw_data.csv"
CLEAN_FILE = Path(__file__).parent / "clean_data.csv"


with (
    open(DATA_FILE, newline="") as fin,
    open("clean_data.csv", "w", newline="") as fout,
):
    ...
