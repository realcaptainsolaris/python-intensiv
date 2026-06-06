"""
Python Integer, floats und arithmetische Operatoren

In Python werden Ganzzahlen als Integer bezeichnet und durch den Datentyp
`int` repräsentiert. Arithmetische Operatoren erlauben mathematische
Berechnungen wie Addition, Subtraktion, Multiplikation und Division.
Hierbei sind auch fortgeschrittene Operatoren wie Modulo oder
Exponentialrechnung verfügbar.

Python Floats sind 64 bit Gleitkommazahlen nach IEEE 754 (C double).

Besonderheiten:
- Integer in Python haben keine feste Größenbeschränkung, sondern nur
  eine Speichergrenze durch die verfügbare Hardware.
- Division mit `/` erzeugt immer einen Fließkommawert (float), selbst
  wenn das Ergebnis mathematisch eine Ganzzahl ist.

Beispiele für arithmetische Operatoren:
- Addition: `+`
- Subtraktion: `-`
- Multiplikation: `*`
- Division: `/`
- Modulo: `%`
- Potenzierung: `**`
- Ganzzahlige, nach unten gerundete Division (Floor Division): `//`
- Ganzzahlige Division (Floor Division): `//`
  - Das Ergebnis der Division wird auf die nächstkleinere ganze Zahl abgerundet (Floor).
  - Beispiel: `7 // 3` ergibt `2`
  - Beispiel: `-7 // 3` ergibt `-3`

Weitere nützliche builtin Funktionen:
- `sum()`: Summiert alle Werte in einer Sequenz.
- `min()`: Gibt den kleinsten Wert einer Sequenz oder der Argumente wieder
- `max()`: Gibt den größten Wert einer Sequenz zurück oder der Argumente wieder.

Strings und andere Datentypen können nach Bedarf in Integer umgewandelt werden,
z. B. mit der Funktion `int()`. Dabei muss die Zeichenkette eine gültige Ganzzahl
darstellen, andernfalls wird eine Fehlermeldung (ValueError) ausgelöst.
x = int("42")  # Ergebnis: 42
type(x)  # Ergebnis: <class 'int'>
"""

import math
