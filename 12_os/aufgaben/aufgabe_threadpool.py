"""
Aufgabe: Parallelisierte Berechnung mit ThreadPoolExecutor

Ziel:
Üben Sie, wie man rechenintensive oder zeitaufwändige Aufgaben
mit einem ThreadPoolExecutor parallelisiert und die Ergebnisse
über Future-Objekte einsammelt.

Beschreibung:
Ein Labor misst regelmäßig Sensordaten. Für jede Sensordatei
soll die Durchschnittstemperatur berechnet werden.
Die Funktion `analyze_sensor(file)` liest die Werte und gibt
den Mittelwert zurück.

Sie sollen:
1. Die Dateien aus SENSOR_FILES parallel verarbeiten.
2. Die Ergebnisse einsammeln, sobald sie fertig sind (as_completed).
3. Exceptions behandeln (z. B. fehlerhafte Datei).
4. Am Ende alle Mittelwerte als Dictionary ausgeben:
       {"sensor1.csv": 22.3, "sensor2.csv": 18.9, ...}

Beispielausgabe:
    Fertig: sensor3.csv -> 19.2 °C
    Fehler bei sensor4.csv: Datei beschädigt
    Ergebnisse: {'sensor1.csv': 20.1, 'sensor2.csv': 18.9, 'sensor3.csv': 19.2}

Hinweise:
- Verwenden Sie ThreadPoolExecutor(max_workers=3)
- Nutzen Sie `as_completed`, um Ergebnisse in Fertigstellungsreihenfolge zu verarbeiten.
"""

import csv
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


# Beispielhafte Sensordateien (in Realität lägen hier echte CSV-Dateien vor)
SENSOR_FILES = [f"sensor{i}.csv" for i in range(1, 6)]


def analyze_sensor(filename: str) -> float:
    """Simuliert das Einlesen und Auswerten einer Sensordatei."""
    time.sleep(random.uniform(0.5, 2.0))  # simulierte Rechenzeit
    if random.random() < 0.2:
        raise ValueError("Datei beschädigt")  # zufälliger Fehler
    temperatures = [random.uniform(15, 25) for _ in range(100)]
    return sum(temperatures) / len(temperatures)


# Ihre Lösung hier
# Tipp:
# - executor.submit(analyze_sensor, filename)
# - as_completed für Ergebnisverarbeitung
# - try/except um Fehler pro Future abzufangen
