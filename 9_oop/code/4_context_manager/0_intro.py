"""
Thema: Kontext-Manager in Python – with-Anweisung und __enter__/__exit__

Kontext-Manager dienen dazu, Ressourcen sicher zu verwalten – z. B. Dateien,
Netzwerkverbindungen oder Sperren (Locks). Sie stellen sicher, dass Ressourcen
am Ende immer korrekt freigegeben werden, selbst wenn Fehler auftreten.

Grundidee:
- Beim Eintritt in den Kontext (`with`) wird automatisch __enter__() aufgerufen.
- Beim Verlassen des Kontexts (auch bei Exceptions) wird __exit__() ausgeführt.

Beispiel:
    with open("data.txt", "r") as f:
        content = f.read()
    # Datei ist hier automatisch geschlossen

Das ist äquivalent zu:
    f = open("data.txt", "r")
    try:
        content = f.read()
    finally:
        f.close()

Das Konzept ist ähnlich wie RAII in C++ (Resource Acquisition Is Initialization).
"""
