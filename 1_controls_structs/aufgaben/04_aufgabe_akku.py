"""
Aufgabe:
Ein Akku-Simulator soll den Ladezustand eines Geräts verfolgen.
Zu Beginn beträgt der Ladezustand 50 %.
Pro Schleifendurchlauf wird der Akku um 7 % entladen.
Wenn der Ladezustand unter 20 % fällt, soll automatisch eine „Energiesparmodus aktiviert“-Meldung erscheinen.
Wenn der Ladezustand auf 0 % fällt oder darunter, soll die Schleife enden mit der Meldung „Akku leer – System heruntergefahren“.

Zusätzlich soll der Benutzer gefragt werden, ob das Gerät an den Strom angeschlossen wird:
Wenn die Eingabe „laden“ lautet, steigt der Akkustand pro Schleife um 10 %.
Wenn die Eingabe leer bleibt, läuft die Entladung weiter.

Beispiel (interaktive Simulation):
Ladezustand: 50 %
> laden
Ladezustand: 60 %
>
Ladezustand: 53 %
..
>
Ladezustand: 18 %
Energiesparmodus aktiviert
>
Ladezustand: 11 %
>
Ladezustand: 4 %
>
Ladezustand: -3 %
Akku leer – System heruntergefahren
"""

akku = 50
