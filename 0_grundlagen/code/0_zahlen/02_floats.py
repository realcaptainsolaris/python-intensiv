"""
Fließkommazahlen in Python: Stellen, Präzision und Probleme

Fließkommazahlen werden in Python mit dem Typ `float` dargestellt. Dieser
ermöglicht die Darstellung von Dezimalzahlen und unterstützt auch die
wissenschaftliche Notation. Allerdings gibt es wichtige Aspekte und
Einschränkungen, die beachtet werden sollten.

Er enstpricht dem C Datentyp double (64 bit), und ist in IEEE 754 spezifiziert.

Rundung: mit der eingebauten Funktion round() lassen sich Fließkommazahlen runden
x = round(3.14159, 2)  # Ergebnis: 3.14

Das Rundungsverhalten von round() ist "round half to even" (Banker's Rounding).
Für kaufmännische Anwendungen sollte das Decimal Modul verwendet werden.
"""
