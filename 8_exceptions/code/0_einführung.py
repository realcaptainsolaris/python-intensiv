"""
Das Thema dieser Datei ist eine Einführung in das Exception Handling in Python.

- Exceptions treten auf, wenn im Programm ein Fehler auftritt.
- Mit Exception Handling können Fehler abgefangen und behandelt werden,
  ohne dass das Programm abstürzt.
- Die wichtigsten Keywords sind `try`, `except`, `else` und `finally`.
"""

# Beispiel 1: Grundlagen des Exception Handling


def divide(a, b):
    """Teilt zwei Zahlen und behandelt Division durch Null."""
    pass


# Beispielaufrufe der Funktion
print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Fehler

# Beispiel 2: Mehrere Exceptions abfangen


def convert_to_int(value):
    """Konvertiert einen Wert in einen Integer und behandelt Fehler."""
    pass


# Beispielaufrufe der Funktion
print(convert_to_int("123"))  # 123
print(convert_to_int("abc"))  # Fehler
print(convert_to_int(None))  # Fehler


# Beispiel 3: Nutzung von `else` und `finally`


def read_file(file_path):
    """Liest eine Datei ein und behandelt mögliche Fehler."""
    pass


# Beispielaufruf der Funktion
# Erstelle eine Datei und teste den Aufruf mit verschiedenen Pfaden.
# print(read_file("example.txt"))
# print(read_file("missing.txt"))
