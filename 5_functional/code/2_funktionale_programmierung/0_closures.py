"""
Eine Closure ist ein Konzept aus der funktionalen Programmierung.
Wenn eine Funktion, die freie Variablen verwendet, den Scope verlässt,
in dem diese vereinbart sind (meistens, weil sie selbst von einer Funktion
zurückgegeben wird), und wird dieser Scope abgeräumt, so wären diese
freien Variablen ab diesem Zeitpunkt undefiniert.

Um dem zu begegnen, setzt der Compiler bei der Rückgabe eine neue Struktur
zusammen. Sie besteht aus dieser Funktion und sämtlichen von ihr
verwendeten freien Variablen. Diese Struktur heißt Closure.

Ein Closure entsteht, wenn:
1. Eine Funktion innerhalb einer anderen definiert ist,
2. Die innere Funktion eine Variable der äußeren Funktion verwendet,
3. Die äußere Funktion eine Referenz auf die innere Funktion zurückgibt.

Closures ermöglichen das Erzeugen spezialisierter Funktionen zur
Laufzeit und werden oft für Konfiguration, Kapselung und in
funktionalen Programmiertechniken verwendet.

Real-World-Beispiel: Ein Rabatt-Generator, der je nach eingegebenem
Rabattprozentsatz eine angepasste Preisfunktion erzeugt.
"""


# Beispiel 1: Einfache Closure zur Erzeugung einer Multiplikationsfunktion

# Beispiel 2: Closure zur Rabattberechnung


# Aufgabe: Erzeuge mit einem Closure eine Funktion, die zu einem
# beliebigen Text einen bestimmten Suffix anhängt

# Funktionsweise
# add_html = suffix_anhänger(".html")
# print(add_html("index"))  # index.html

# add_ausrufezeichen = suffix_anhänger("!!!")
# print(add_ausrufezeichen("Wow"))  # Wow!!!
