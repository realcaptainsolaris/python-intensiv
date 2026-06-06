"""
Das Thema dieser Datei ist die Arbeit mit Dateioperationen in Python.

- Python bietet zahlreiche Funktionen, um Dateien zu lesen, zu schreiben
"""

# 1. Datei erstellen und schreiben
from pathlib import Path

file_name = Path(__file__).parent / "example.txt"
