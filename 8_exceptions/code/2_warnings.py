"""
Einführung in das warnings-Modul

In Python sind **Warnings (Warnungen)** keine echten Fehler, sondern Hinweise darauf,
dass etwas potenziell problematisch ist – das Programm läuft aber weiter.
Sie werden häufig verwendet, um vor unsauberem oder zukünftig veraltetem Verhalten zu warnen,
ohne den Code sofort zu stoppen.

Die Warnungen werden mit dem Modul `warnings` erzeugt und gesteuert.
https://docs.python.org/3/library/exceptions.html

import warnings
warnings.warn("Diese Funktion ist veraltet", DeprecationWarning)

Das Programm zeigt eine Warnung an, bricht aber nicht ab.

Typische Warning-Klassen:
- UserWarning: allgemeine Warnung
- DeprecationWarning: etwas wird in Zukunft entfernt oder geändert
- ResourceWarning: z. B. wenn Dateien nicht geschlossen wurden
- RuntimeWarning: ungewöhnliche Laufzeitbedingungen

Warnungen lassen sich filtern oder unterdrücken, z. B.:

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

"""

import warnings
