"""
Dieses Modul gibt eine Einführung in den sogenannten "Walrus Operator"
(:=), der mit Python 3.8 eingeführt wurde.

Er erlaubt es, einer Variablen **während** eines Ausdrucks einen Wert
zuzuweisen. Das reduziert doppelte Berechnungen und erlaubt kompaktere,
aber weiterhin lesbare Code-Konstruktionen.

Syntax:
    variable := Ausdruck

Typische Anwendungen:
- While-Schleifen mit Input oder IO
- Bedingungen, die gleichzeitig speichern und prüfen
- List Comprehensions mit Bedingungsspeicherung

Hinweis: Der Operator hat seine Grenzen und sollte nur dort verwendet
werden, wo er wirklich Klarheit schafft.

Hinweis: Der Walrus-Operator (:=) hat eine geringere Priorität als viele
andere Operatoren – daher sollte er in komplexeren Ausdrücken immer in
Klammern gesetzt werden, um unerwartetes Verhalten zu vermeiden.
"""
