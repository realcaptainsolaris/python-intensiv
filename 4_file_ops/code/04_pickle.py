"""
Das Thema dieser Datei ist die Verwendung des `pickle`-Moduls in Python.

- `pickle` ist ein Modul der Python-Standardbibliothek zur Serialisierung
  und Deserialisierung von Python-Objekten.
- Serialisierung bedeutet, ein Python-Objekt in ein Byte-Format umzuwandeln,
  das gespeichert oder übertragen werden kann.
- Deserialisierung ist der Prozess, dieses Byte-Format wieder in ein Python-Objekt
  zurückzuverwandeln.
- Mit `pickle` können auch komplexe Python-Objekte wie Listen, Dictionaries,
  Instanzen eigener Klassen oder Machine Learning Modelle gespeichert werden.

Wichtiger Sicherheitshinweis:

Beim Laden von Pickle-Daten (`pickle.load()` oder `pickle.loads()`) kann
beliebiger Python-Code ausgeführt werden. Deshalb dürfen Pickle-Dateien
niemals aus nicht vertrauenswürdigen Quellen geladen werden.

Pickle ist kein sicheres Austauschformat und sollte nur für Daten verwendet
werden, die von der eigenen Anwendung erzeugt wurden oder aus einer
vertrauenswürdigen Quelle stammen.

Alternativen:

- `json` für plattformunabhängige und sichere Datenaustauschformate.
- `sqlite3` für strukturierte und persistente Datenspeicherung.
- `csv` für tabellarische Daten.
"""

from pathlib import Path
import pickle

# 1. Einführung in das `pickle`-Modul
# Beispiel-Daten
data = {
    "name": "Anna",
    "age": 30,
    "languages": ["Deutsch", "Englisch"],
    "is_employed": True,
}

# 2. Serialisierung: Schreiben von Objekten in eine Datei
file_path = Path(__file__).parent / "data.pkl"
