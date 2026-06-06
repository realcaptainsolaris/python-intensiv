"""
Slicing von Sequencen in Python

Slicing erlaubt es, Teilstrings (Substrings) aus einem String zu
extrahieren. Das Prinzip lässt sich auf alle Sequenztypen in Python anwenden,
einschließlich Listen.

Mit Hilfe von Start-, End- und Schrittwerten kann flexibel auf bestimmte
Abschnitte eines Strings zugegriffen werden.

Die Slice-Notation
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String

a[start:stop:schrittweite]  # beginnt bei Start und endet bei Stop - 1 in Schrittweite
"""

# # Übung
# # Schneide jeweils alle A aus den Strings
# BBAAABBB => AAA
# AAAABBBB => AAAA
# ABBBBB => A
string = "AAAAB"
print(string[0:4])

string = "BBAAABBB"

string = "AAAABBBB"

string = "ABBBBB"
