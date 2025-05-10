"""
In Python bezeichnet man als **Iterable** ein Objekt, über das man
iterieren kann – z. B. Listen, Tupel, Strings oder Generatoren.
Ein **Iterator** ist ein Objekt, das den aktuellen Zustand einer
Iteration speichert und über `next()` das nächste Element liefert.

Ein Iterable liefert beim Aufruf von `iter()` einen Iterator.
Ein Iterator besitzt die Methoden `__iter__()` und `__next__()`.

iter() kann explizit aufgerufen werden, um einen Iterator zu erzeugen.
iter() wird auch implizt aufgerufen, zb. bei einem for-loop oder
der map()-Funktion.

Beispiel: Listen sind iterierbar, aber keine Iteratoren. Erst der Aufruf
von `iter(liste)` erzeugt einen Iterator, der mit `next()` verwendet
werden kann.

Dieses Skript zeigt den Unterschied anhand praktischer Beispiele.
"""
