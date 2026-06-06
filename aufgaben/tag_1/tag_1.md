# Nachmittagsprojekt: Movie Catalog Service

## Tag 1: Filme verwalten

### Ziel

Heute entwickelst du den ersten Teil eines kleinen Movie Catalog Service.

Das System soll Filme verwalten, durchsuchen und filtern können. Die Daten werden zunächst ausschließlich im Speicher gehalten. Datenbanken, Dateien und APIs folgen in den kommenden Tagen.

Dabei setzt du die bisher gelernten Python-Konzepte praktisch ein:

* Listen
* Dictionaries
* Funktionen
* Kontrollstrukturen
* Schleifen
* Type Hints
* Saubere Programmstruktur

---

## Ausgangsdaten

Du arbeitest mit einer Liste von Filmen.
Jeder Film besitzt mindestens folgende Informationen:

```python
{
    "title": "The Matrix",
    "year": 1999,
    "genre": "Sci-Fi",
    "rating": 8.7,
}
```
Die Filme sind gegeben in der Datei `tag_1.py`.


---

## Alle Filme anzeigen

Implementiere die Funktion `print_movies`.

Die Funktion soll alle ihr übergebenen Filme übersichtlich auf der Konsole ausgeben.
Sie hat keinen Rückgabewert, sondern gibt die Informationen direkt aus.
Achte auf richte Typehints und einen Doc-String.

Beispielausgabe:

```text
The Matrix (1999) - Sci-Fi - 8.7
Alien (1979) - Sci-Fi - 8.5
Gladiator (2000) - Action - 8.4
```

Die Funktion wird so aufgerufen (mit allen Filmen):
```python
print_movies(movies)
```

---

## Filme nach Genre filtern

Implementiere die Funktion `filter_by_genre`.

Die Funktion soll alle Filme eines bestimmten Genres zurückgeben.
Rückgabe ist eine Liste von Dictionaries, die den Filmen entsprechen.
Die Rückgabe muss dann mit `print_movies` ausgegeben werden.

Beispiel:

```python
sci_fi_movies = filter_by_genre(
    movies,
    "Sci-Fi",
)
print_movies(sci_fi_movies)
```
Beispielausgabe:

```text
The Matrix (1999) - Sci-Fi - 8.7
Alien (1979) - Sci-Fi - 8.5
```

---

## Filme ab einem bestimmten Jahr

Implementiere die Funktion `movies_after_year`.

Die Funktion soll alle Filme zurückgeben, die ab einem bestimmten Jahr veröffentlicht wurden.
Nutze einen arithmetischen Vergleichsoperator, um die Filme zu filtern und einer neuen Liste hinzuzufügen.
Nutze wieder die Funktion `print_movies`, um die Ergebnisse anzuzeigen.

Beispiel:

```python
recent_movies = movies_after_year(
    movies,
    2010,
)
```

---

## Nach Titel suchen

Implementiere die Funktion `search_movies`.

Die Funktion soll Filme anhand eines Suchbegriffs im Titel finden und als Liste von Dicts zurückgeben.
Die Suche soll nicht zwischen Groß- und Kleinschreibung unterscheiden. Nutze dazu die String-Methode `lower()`
und den `in`-Operator.

Nutze wieder die Funktion `print_movies`, um die Ergebnisse anzuzeigen

Beispiel:

```python
results = search_movies(
    movies,
    "matrix",
)
```

---

## Statistiken berechnen

### Durchschnittliche Bewertung

Implementiere die Funktion `average_rating`.

Die Funktion soll die durchschnittliche Bewertung aller Filme berechnen.
Rückgabewert ist eine Fließkommazahl, die die durchschnittliche Bewertung angibt.


Beispiel:

```python
rating = average_rating(movies)
print(rating)
```

```text
8.41
```

### Filme pro Genre zählen

Implementiere die Funktion `movie_count_per_genre`.
Die Funktion soll zählen, wie viele Filme pro Genre vorhanden sind (Frequenzzählung).

Verwende ein Dictionary, bei dem das Genre der Schlüssel und die Anzahl der Filme der Wert ist.
Falls das Genre noch nicht im Dictionary vorhanden ist, füge es mit einem Wert von 1 hinzu. 
Falls es bereits vorhanden ist, erhöhe den Wert um 1.
RÜckgabewert ist dieses Dictionary.

Überlege dir, wie du danach die Ergebnisse übersichtlich auf der Konsole ausgeben kannst.

Beispielausgabe:

```text
Sci-Fi: 4
Action: 3
Drama: 2
```

---

## Bonusaufgabe 1

Implementiere die Funktion `best_movie_per_genre`.
Die Funktion soll für jedes Genre den Film mit der höchsten Bewertung ermitteln.
RÜckgabe ist ein dict mit Genre als Schlüssel und der Value der Film (dict) (`dict[str, dict]`). 

Ähnlich wie die Augabe zuvor. Statt der Anzahl der Filme zu zählen, soll immer geprüft werden, ob die Bewertung des aktuellen Films höher ist als die bisher gespeicherte Bewertung für dieses Genre.


Beispiel:

```text
Sci-Fi -> Interstellar
Drama -> Forrest Gump
Action -> The Dark Knight
```

---

## Bonusaufgabe 2

Erstelle ein kleines Konsolenmenü.
Ein, zwei Menüpunkte reichen.

Beispiel:

```text
Movie Catalog

1 - Alle Filme anzeigen
2 - Nach Genre filtern
3 - Nach Titel suchen
5 - Statistiken anzeigen
0 - Beenden
```

Verwende dazu `if` oder `match`.
