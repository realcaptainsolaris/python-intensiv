"""
Aufgabe:
Gegeben ist ein verschachteltes Wörterbuch (Dictionary), das Informationen über eine Person enthält.
Einige Werte sind selbst wieder Dictionaries (z. B. Kontaktinformationen).

Schreibe eine Funktion `find_key(d, target)`, die rekursiv alle Ebenen durchsucht
und den Wert zu einem bestimmten Schlüssel (`target`) zurückgibt.

Vorgaben:
- Wenn der Schlüssel gefunden wird, gib den zugehörigen Wert zurück.
- Wenn der Schlüssel nicht existiert, gib None zurück.
- Die Funktion soll rekursiv auf Unter-Dictionaries angewendet werden.

Beispiel:
person = {
    "name": "Alice",
    "details": {
        "age": 30,
        "contact": {"email": "alice@example.com", "phone": "123-456"},
    },
}

Aufruf:
>>> find_key(person, "email")

Ausgabe:
'alice@example.com'
"""
