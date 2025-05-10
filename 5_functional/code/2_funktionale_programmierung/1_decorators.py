"""
Ein Decorator (dt. Dekorierer) ist ein Konstrukt in Python, mit dem
Funktionen oder Methoden um zusätzliche Funktionalität erweitert werden
können, ohne ihren eigentlichen Code zu verändern.

Ein Decorator ist eine Funktion, die eine andere Funktion als Argument
nimmt und eine neue Funktion zurückgibt.

Einsatzmöglichkeiten:
- Logging
- Zeitmessung
- Zugriffskontrolle
- Vor- und Nachbedingungen

Syntax:
@decorator_name
def funktion():
    ...

Dies ist gleichbedeutend mit:
funktion = decorator_name(funktion)

Dieses Skript zeigt den grundlegenden Aufbau eines einfachen Decorators.
"""
