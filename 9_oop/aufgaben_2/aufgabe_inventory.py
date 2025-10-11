"""
( mittelschwer )

Thema: Operator Overloading – Inventarverwaltung in einer Fantasywelt

Aufgabe:
Erstellen Sie eine Klasse `Inventar`, die das Gepäck eines Abenteurers repräsentiert.

Anforderungen:
1. Das Inventar speichert Gegenstände und deren Anzahl als Dictionary:
       inv = Inventar({"Trank": 3, "Schwert": 1})
2. Operatoren:
   - inv1 + inv2 → neues Inventar mit kombinierten Gegenständen
   - inv1 - inv2 → neues Inventar nach Verbrauch (keine negativen Mengen)
   - inv1 == inv2 → True, wenn beide Inventare exakt gleich sind
3. __repr__ oder __str__ soll eine lesbare Beschreibung liefern.

Beispiel:

    ritter = Inventar({"Schwert": 1, "Trank": 3})
    magier = Inventar({"Trank": 2, "Zauberbuch": 1})

    print(ritter + magier)
    # {'Schwert': 1, 'Trank': 5, 'Zauberbuch': 1}

    print(ritter - magier)
    # {'Schwert': 1, 'Trank': 1, 'Zauberbuch': 0}

    print(ritter == magier)
    # False

Bonus:
Fügen Sie eine Methode hinzu:
    def gesamtanzahl(self):
        -> gibt die Summe aller Gegenstände zurück.
"""
