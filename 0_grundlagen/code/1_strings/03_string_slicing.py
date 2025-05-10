"""
String Slicing in Python

String Slicing erlaubt es, Teilstrings (Substrings) aus einem String zu
extrahieren.
Mit Hilfe von Start-, End- und Schrittwerten kann flexibel auf bestimmte
Abschnitte eines Strings zugegriffen werden.

Themenübersicht:
1. Grundlagen des Slicings
2. Negative Indizes
3. Slicing mit Schrittwerten
4. Nützliche Anwendungen



Die Slice-Notation
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String
"""

# # Übung
# # Schneide jeweils alle A aus den Strings
# AAAAB => AAAA
# BBAAABBB => AAA
# AAAABBBB => AAAA
# ABBBBB => A
string = "AAAAB"

string = "BBAAABBB"

string = "AAAABBBB"

string = "BBAABBBB"

string = "ABBBBB"
