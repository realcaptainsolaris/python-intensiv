"""
Schwer

Gegeben ist eine Zahl n und ein Name.
Drucke den Namen n-mal aus wie im Beispiel gezeigt:

name = Paul
n = 4

Output:
P|a|u|l P|a|u|l P|a|u|l P|a|u|l

Hinweis 1: die String-Methode join kann eine ihr übergebene Sequenz
anhand eines Trenners (String) zu einem neuen String zusammenfügen
ein String ist eine Sequenz.
"*".join("abc"]) => "a*b*c"

Hinweis 2: auf die Liste kann der Multiplikations-Operator angewandt werden.
Das Ergebnis ist eine neue Liste, die die Elemente der Ursprungs-Liste enthält
["*"] * 3 => ["*", "*", "*"]

"""

name = "Paul"
n = 4
separator = "|"
