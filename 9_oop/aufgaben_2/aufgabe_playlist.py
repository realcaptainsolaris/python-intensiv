"""
Aufgabe Playlist

Erstelle zwei Klassen: `Song` und `Playlist`.

1. Klasse `Song`
   Attribute:
       - title (str)
       - artist (str)
       - duration (int, in Sekunden)

   Methode:
       - __repr__: Gibt eine lesbare Darstellung aus, z. B.
         Song(title='Africa', artist='Toto', duration=295)

2. Klasse `Playlist`
   Attribute:
       - name (z. B. "Roadtrip Mix")
       - songs (Liste von Song-Objekten)

   Methoden:
       - add_song(song): fügt einen Song hinzu
       - remove_song(song): entfernt einen Song (nach Titelvergleich)
       - total_duration(): berechnet die Gesamtdauer in Minuten (gerundet)
       - __iter__: erlaubt das Durchlaufen der Playlist mit einer for-Schleife

Beispiel:

    s1 = Song("Africa", "Toto", 295)
    s2 = Song("Billie Jean", "Michael Jackson", 294)
    pl = Playlist("80s Hits")
    pl.add_song(s1)
    pl.add_song(s2)

    for song in pl:
        print(song)

    print("Gesamtdauer:", pl.total_duration(), "Minuten")

Erwartete Ausgabe:
    Song(title='Africa', artist='Toto', duration=295)
    Song(title='Billie Jean', artist='Michael Jackson', duration=294)
    Gesamtdauer: 10 Minuten
"""
