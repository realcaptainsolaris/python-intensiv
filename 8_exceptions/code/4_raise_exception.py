"""
Einführung in 'raise'

Mit 'raise' kannst du in Python gezielt eine Exception (Fehler) auslösen.
Das ist nützlich, wenn du ungültige Zustände erkennst oder Eingaben prüfen willst.

Beispiel:
    x = -5
    if x < 0:
        raise ValueError("x darf nicht negativ sein")

Das Programm stoppt an dieser Stelle mit einer Fehlermeldung.

Hinweis:
- Mit 'raise' ohne Argument in einem except-Block wird die aktuelle Exception erneut ausgelöst.
- Verwende spezifische Exception-Typen (z. B. ValueError, TypeError) statt einer allgemeinen Exception.
"""
