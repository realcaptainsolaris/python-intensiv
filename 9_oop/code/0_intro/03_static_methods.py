"""
Thema: Statische Methoden in Python – @staticmethod

Statische Methoden gehören zur Klasse, nicht zur Instanz. Sie werden
mit dem Decorator @staticmethod gekennzeichnet und benötigen weder
self noch cls als ersten Parameter.

Sie können wie normale Funktionen definiert werden, sind aber zur
besseren Strukturierung an die Klasse gebunden – z. B. für Hilfsfunktionen,
die logisch zur Klasse gehören, aber keinen Zugriff auf Instanz- oder
Klassendaten benötigen.

Aufruf: direkt über Klasse oder Instanz möglich (Klasse.methode()).

Vergleich zu anderen Sprachen:
- In **Java** und **C++** entsprechen @staticmethod-Methoden den dortigen
  `static`-Methoden einer Klasse.
  Auch dort sind sie Teil der Klasse, werden aber ohne Objektkontext aufgerufen.

- In Python ist der Unterschied, dass statische Methoden nur durch den
  Decorator @staticmethod markiert werden – kein Schlüsselwort `static` nötig.

- Zudem ist Python dynamischer: eine statische Methode kann auch nachträglich
  zur Klasse hinzugefügt oder ersetzt werden.
"""
