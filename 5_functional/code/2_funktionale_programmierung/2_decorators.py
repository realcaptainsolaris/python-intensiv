"""
Parametrisierte Decorators erlauben es, einem Decorator Argumente zu
übergeben. Das ist besonders nützlich, wenn das Verhalten des Decorators
abhängig von konfigurierbaren Werten sein soll – etwa bei Validierungen,
Log-Leveln oder bedingtem Ausführen.

Ein parametrisierter Decorator besteht aus drei verschachtelten Funktionen:
1. Eine äußere Funktion, die die Parameter des Decorators entgegennimmt.
2. Eine innere Decorator-Funktion, die die zu dekorierende Funktion annimmt.
3. Ein Wrapper, der die Logik ausführt.

Dieses Skript zeigt reale Anwendungsbeispiele für Decorators mit Parametern,
zum Beispiel zur Wertevalidierung und Zugriffskontrolle.
"""


# Beispiel 1: Validierung von Zahlenwerten mit einem parameterisierten Decorator


# @validate_range(1, 10)
def quadrat(x):
    return x * x


# print(quadrat(3))  # gültig
# print(quadrat(20))  # ValueError


# Beispiel 2: Zugriffskontrolle basierend auf Rollen

# admin_user = {"name": "Anna", "rolle": "admin"}
# print(starte_server(admin_user))  # Server gestartet!

# normal_user = {"name": "Ben", "rolle": "user"}
# print(starte_server(normal_user))  # PermissionError


# Beispiel 3: Real-World: Decorator für Texteingaben mit Mindestlänge
# @min_textlaenge(5)
def speichere_kommentar(text):
    return f"Kommentar gespeichert: {text}"


# print(speichere_kommentar("Sehr gut!"))
# print(speichere_kommentar("Hi"))  # ValueError
