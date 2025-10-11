"""
Beispiel: Verwendung des warnings-Moduls zur Kommunikation mit Entwicklern.

Angenommen, eine Bibliothek soll dem Benutzer mitteilen,
dass eine Funktion bald entfernt oder ihr Verhalten geändert wird.
Das ist kein Laufzeitfehler – aber ein Hinweis für Entwickler,
ihren Code anzupassen.
"""

import warnings


def calculate_mean(values, *, ignore_none=False):
    if not ignore_none:
        warnings.warn(
            "Parameter 'ignore_none=False' wird in zukünftigen Versionen entfernt. "
            "Bitte 'ignore_none=True' verwenden.",
            DeprecationWarning,
            stacklevel=2,  # Level im Callstack, 2 => bei Aufruf der funktion
        )

    cleaned = [v for v in values if v is not None]
    return sum(cleaned) / len(cleaned)


# Beispielaufruf – simuliert alten Code
data = [10, None, 20]
print("Ergebnis:", calculate_mean(data, ignore_none=False))
