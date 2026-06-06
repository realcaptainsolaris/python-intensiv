# Nachmittagsprojekt: Movie Catalog Service

## Tag 3: Objektorientierung und Projektstruktur

### Ziel

Bisher wurden Filme als Dictionaries verarbeitet.

Heute wird die Anwendung grundlegend umgebaut. Statt Dictionaries sollen echte Python-Objekte verwendet werden. Außerdem wird das Projekt in eine professionelle Paketstruktur überführt.

Heute werden insbesondere folgende Themen angewendet:

* uv
* Flat-Layout
* Pakete
* Module
* Importe
* `__init__.py`
* Dataclasses
* Objektorientierung
* Klassen
* Methoden

---

## Ausgangssituation

Aktuell arbeitet die Anwendung mit Dictionaries:

```python
{
    "title": "The Matrix",
    "year": 1999,
    "genre": "Sci-Fi",
    "rating": 8.7,
    "country": "USA",
}
```

Zukünftig soll stattdessen mit Objekten gearbeitet werden:

```python
movie.title
movie.year
movie.genre
```

---

## Aufgabe 1: Neues Projekt mit uv erstellen (Flat Layout)

Erstelle ein neues Projekt:

```bash
uv init movie_catalog
cd movie_catalog

mkdir movie_catalog
touch movie_catalog/__init__.py
touch movie_catalog/main.py
```

Das sieht dann so aus

```text
movie_catalog/
│
├── pyproject.toml
│
└── movie_catalog/
    ├── __init__.py
    ├── main.py
```

Im äußeren Ordner befindet sich die Projektdatei `pyproject.toml`. In realen Projekten liegt hier auch die Dokumentation, Tests und weitere Dateien, zb. Infrastruktur (`docker-compose`, `tox.ini`, etc.)


Als Alternative zu `touch` können die Dateien natürlich auch direkt über den Editor angelegt werden.

Untersuche anschließend die erzeugte Struktur.
Starte das Projekt anschließend:

```bash
uv run -m movie_catalog.main
```
Das startet die Datei `main.py` im Paket `movie_catalog`.
Mache ein print-Statement in `main.py`, um zu überprüfen, ob alles funktioniert.

---

## Aufgabe 2: Projektstruktur erweitern

Erweitere die Struktur des Projekts um zwei Paktete: `models` und `services`.
Jedes Paket soll eine `__init__.py`-Datei enthalten.

```text
movie_catalog/
│
├── pyproject.toml
│
└── movie_catalog/
    ├── __init__.py
    ├── main.py
    │
    ├── models/
    │   ├── __init__.py
    │   └── movie.py
    │
    └── services/
        ├── __init__.py
        └── movie_service.py
```

## Aufgabe 3: Movie als Dataclass modellieren

### Klasse

`Movie`

### Attribute

* title
* year
* genre
* rating
* country

### Aufgabe

Erstelle eine Dataclass zur Beschreibung eines Films.

Anschließend sollen Filme nicht mehr als Dictionaries, sondern als Objekte angelegt werden.

Beispiel:

```python

matrix_movie = Movie(
    title="The Matrix",
    year=1999,
    genre="Sci-Fi",
    rating=8.7,
    country="USA",
)
```

## Aufgabe 4: Filme als Objekte verwalten

Erstelle mehrere Filmobjekte.
Speichere sie in einer Liste.
Gebe die Filme mit der Funktion `print_movies` von gestern aus, 
passe diese Funktion aber so an, dass sie mit Movie-Objekten statt mit Dictionaries arbeitet.
Lege sie in `main.py` an.

Beispiel:

```python
movies = [
    Movie(...),
    Movie(...),
    Movie(...),
]
print_movies(movies)
```
---

## Aufgabe 5: MovieService erstellen

### Klasse

`MovieService`

### Aufgabe

Erstelle eine Klasse, die eine Filmliste verwaltet.
Der Konstruktor soll eine Liste von Filmen übernehmen.

Beispiel Aufruf in `main.py`:

```python
service = MovieService(
    movies,
)
```

---

## Aufgabe 6: Filme nach Genre suchen

### Methode

`find_by_genre`

### Parameter

* Genre

### Rückgabewert

* Liste passender Filme als Liste von Movie-Objekten

Beispiel:

```python
result = service.find_by_genre(
    "Sci-Fi",
)
print_movies(result)
```

---

## Aufgabe 7: Filme nach Jahr filtern

### Methode

`find_after_year`

### Parameter

* Jahr

### Rückgabewert

* Liste passender Filme

### Aufgabe

Liefere alle Filme zurück, die ab einem bestimmten Jahr erschienen sind.

Beispiel:

```python
result = service.find_after_year(
    2010,
)
print_movies(result)
```

---

## Aufgabe 8: Nach Titel suchen

### Methode

`search`

### Parameter

* Suchbegriff

### Rückgabewert

* Liste passender Filme

### Aufgabe

Durchsuche alle Filmtitel.

Die Suche soll Groß- und Kleinschreibung ignorieren.

Beispiel:

```python
result = service.search(
    "matrix",
)
print_movies(result)
```

---

## Aufgabe 9: Top-Filme ermitteln

### Methode

`top_movies`

### Parameter

* Anzahl der gewünschten Filme

### Rückgabewert

* Liste der bestbewerteten Filme

### Aufgabe

Sortiere die Filme nach Bewertung und liefere die besten Filme zurück.
Nutze dazu die eingebaute Funktion `sorted` und einen passenden Sortierschlüssel.

Beispiel:

```python
result = service.top_movies(
    5,
)

```

---

## Aufgabe 10: Exporte über **init**.py

Importiere Klassen nicht mehr direkt aus den einzelnen Dateien.

Statt in `main.py`:

```python
from movie_catalog.models.movie import Movie
```

soll künftig folgendes möglich sein:

```python
from movie_catalog.models import Movie
```

Exportiere dazu die Klassen über die jeweiligen `__init__.py`-Dateien.
Teste anschließend alle Importe.

---

## Bonusaufgabe: Pydantic (Falls noch nicht besprochen, bitte ignorieren)

Installiere Pydantic:

```bash
uv add pydantic
```

Erstelle zusätzlich ein Pydantic-Modell in `models/movie.py`.

### Klasse

`MovieModel`

### Attribute

* title
* year
* genre
* rating
* country

### Aufgabe

Validiere die Daten automatisch.

Prüfe beispielsweise:

* Titel darf nicht leer sein
* Jahr muss größer als 1900 sein
* Bewertung muss zwischen 0 und 10 liegen

Beispiel:

```python
movie = MovieModel(
    title="",
    year=1800,
    genre="Sci-Fi",
    rating=15,
    country="USA",
)
```

Untersuche die Fehlermeldungen.
