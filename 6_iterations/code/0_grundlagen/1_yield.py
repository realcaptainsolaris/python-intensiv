"""
Funktionen mit `yield` sind sogenannte Generatorfunktionen.
Statt mit `return` einen Wert zurückzugeben und zu beenden, liefern
sie mit `yield` einen Wert und pausieren ihren Zustand – beim nächsten
Aufruf wird der Code direkt nach dem `yield` fortgesetzt.

Generatorfunktionen erzeugen automatisch einen Iterator und sind
speichereffizient, da sie Werte bei Bedarf liefern (Lazy Evaluation).

Typische Anwendungen:
- Große Datenmengen sequentiell verarbeiten
- Unendliche Sequenzen generieren
- Zustandsbehaftete Abläufe abbilden

Dieses Skript zeigt verschiedene Anwendungsbeispiele für `yield`.
"""
