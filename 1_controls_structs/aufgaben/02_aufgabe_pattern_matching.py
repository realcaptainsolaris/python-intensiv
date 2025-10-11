"""
Gegeben ist eine Liste von Dictionaries mit Informationen zu Büchern:

books = [
    {"title": "Dune", "author": "Herbert", "pages": 412},
    {"title": "It", "author": "King", "pages": 1138},
    {"title": "Foundation", "author": "Asimov", "pages": 255},
    {"title": "Pet Sematary", "author": "King", "pages": 374},
    {"title": "Unbekanntes Werk"}  # fehlerhaftes Beispiel, Autor fehlt
]

Ziel:
- Gib alle Bücher von "King" mit mehr als 400 Seiten aus
- Kennzeichne Bücher mit weniger als 300 Seiten als Kurzroman (in Klammer "Kurzroman")
- Gib alle anderen Bücher mit Titel und Autor aus
- Gib bei unvollständigen Daten (Title/Author oder pages fehlt) eine Warnung aus

Lösung:

Buch: Dune von Herbert
King-Roman mit Überlänge: It (1138 Seiten)
Foundation von Asimov (255 Seiten, Kurzroman)
Buch: Pet Sematary von King
Unvollständige Angabe

Nutze Loop und Pattern Matching (match-case) für die Lösung.
Die Ausgabe soll einfach via print erfolgen.

"""

books = [
    {"title": "Dune", "author": "Herbert", "pages": 412},
    {"title": "It", "author": "King", "pages": 1138},
    {"title": "Foundation", "author": "Asimov", "pages": 255},
    {"title": "Pet Sematary", "author": "King", "pages": 374},
    {"title": "Unbekanntes Werk"},
]
