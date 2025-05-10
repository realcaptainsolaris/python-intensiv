"""
Das Thema dieser Datei ist die Arbeit mit Dateioperationen in Python.

- Python bietet zahlreiche Funktionen, um Dateien zu lesen, zu schreiben
  und zu manipulieren.
- Wir betrachten grundlegende Dateioperationen wie das Erstellen, Lesen,
  Schreiben und Löschen von Dateien.
"""

# 1. Datei erstellen und schreiben
from pathlib import Path

file_name = Path(__file__).parent / "example.txt"
