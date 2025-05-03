"""
Dieses Skript gibt eine Einführung in die Rekursion (recursion) in Python.

**Rekursion** bedeutet, dass sich eine Funktion selbst aufruft, um ein Problem
in kleinere Teilprobleme zu zerlegen. Sie besteht aus:
1. einer Abbruchbedingung (base case)
2. einem rekursiven Schritt, der sich dem Abbruch annähert

Rekursion kann elegante Lösungen für Probleme mit wiederholter Struktur liefern –
zum Beispiel für:
- das Durchlaufen von verschachtelten Strukturen (z. B. Verzeichnisse, JSON)
- das Umwandeln oder Durchsuchen von Baumstrukturen
- das Auflösen von Pfadproblemen

"""


def print_nested_iterativ(data):
    stack = [(data, 0)]  # Start mit äußerer Liste und Einrückung 0

    while stack:
        current, indent = stack.pop()

        # Wir müssen die aktuelle Liste in umgekehrter Reihenfolge abarbeiten,
        # damit beim Auspacken die ursprüngliche Reihenfolge stimmt.
        for item in reversed(current):
            if isinstance(item, list):
                stack.append((item, indent + 2))
            else:
                # Nur wenn es ein Element ist, wird es sofort ausgegeben
                # (also keine Liste, daher tiefste Ebene zuerst)
                print(" " * indent + str(item))


def print_nested(data, indent=0):
    # Beispiel 1: Durchlauf einer verschachtelten Liste
    for item in data:
        if isinstance(item, list):
            print_nested(item, indent + 2)
        else:
            print(" " * indent + str(item))


nested = ["a", ["b", ["c", "d"], "e"], "f"]
print("Verschachtelte Liste:")
# print_nested(nested)
print_nested_iterativ(nested)


# Beispiel 2: Durchsuchen eines verschachtelten Wörterbuchs nach einem Schlüssel
def find_key(d, target):
    for key, value in d.items():
        if key == target:
            return value
        elif isinstance(value, dict):
            result = find_key(value, target)
            if result is not None:
                return result
    return None


person = {
    "name": "Alice",
    "details": {
        "age": 30,
        "contact": {"email": "alice@example.com", "phone": "123-456"},
    },
}

print("Email gefunden:", find_key(person, "email"))


# Beispiel 3: Umwandlung einer Zahl in Binärdarstellung mit Rekursion
def to_binary(n):
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


print("Binär von 13:", to_binary(13))  # 1101
