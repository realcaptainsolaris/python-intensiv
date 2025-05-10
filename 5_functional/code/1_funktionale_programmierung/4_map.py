"""
Die Funktion `map()` ist eine eingebaute Funktion in Python, mit der
man eine Funktion auf jedes Element eines iterierbaren Objekts anwenden
kann. Dabei entsteht ein Iterator mit den Ergebnissen der Anwendung.

Syntax: map(funktion, iterable)

Oft wird `map()` in Kombination mit `lambda` oder einer definierten
Funktion genutzt, um Transformationen effizient durchzuführen.

Wichtig: Der Rückgabewert von `map()` ist ein Iterator, keine Liste.
Will man das Ergebnis als Liste haben, muss man `list()` verwenden.

Reale Anwendungsbeispiele:
- Umrechnung von Einheiten (z. B. Celsius → Fahrenheit)
- Extraktion oder Transformation von Feldern in Datensätzen
- Normalisierung oder Formatierung von Strings

Dieses Skript zeigt den Einsatz von `map()` in mehreren realistischen
Szenarien.
"""

import timeit
