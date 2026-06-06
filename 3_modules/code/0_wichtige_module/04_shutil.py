"""
Das `shutil`-Modul in Python.

- Das `shutil`-Modul bietet Funktionen zum Kopieren, Verschieben und Löschen
  von Dateien und Verzeichnissen sowie zum Arbeiten mit Archiven.
- Es wird häufig für Aufgaben im Zusammenhang mit der Dateiverwaltung verwendet.
"""

from pathlib import Path
import shutil

# --- Datei kopieren ---
source_file = Path(__file__).parent / "source.txt"
destination_file = Path(__file__).parent / "destination.txt"

source_dir = Path(__file__).parent / "data"
destination_dir = Path(__file__).parent / "backup"
