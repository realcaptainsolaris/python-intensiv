"""
( mittelschwer )

Thema: Schnittmengen mit Sets

In einer Welt gibt es drei Gilden: Krieger, Magier und Diebe.
Jede Gilde hat eine Liste mit magischen Artefakten, die sie besitzt.

Gesucht:
Finde heraus, welche Artefakte **alle drei Gilden gemeinsam** besitzen.

Hinweis:
- Nutzen Sie die Schnittmenge (intersection) oder den Operator &.
- Das Ergebnis soll eine Menge sein, die nur die gemeinsamen Artefakte enthält.

Beispiel:
    krieger = {"Schwert", "Schild", "Amulett"}
    magier = {"Amulett", "Zauberstab", "Buch"}
    diebe = {"Dolch", "Seil", "Amulett"}

Ergebnis:
    {"Amulett"}

Erweiterung:
Geben Sie außerdem aus, welche Artefakte **mindestens eine** der Gilden besitzt
"""

krieger = {"Schwert", "Schild", "Amulett", "Rüstung"}
magier = {"Amulett", "Zauberstab", "Buch", "Schild"}
diebe = {"Dolch", "Seil", "Amulett", "Schild"}
