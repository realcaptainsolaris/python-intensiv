r"""
Thema: Reguläre Ausdrücke (Regex) in Python

Dieses Skript vermittelt grundlegende und fortgeschrittene Konzepte
zur Nutzung von regulären Ausdrücken mit dem Modul `re`. Es deckt
Metazeichen, Quantoren, Gruppen, Anker, Identifizierer und Ersetzungen ab.

Nützliche Ressourcen:
https://cheatography.com/davechild/cheat-sheets/regular-expressions/pdf/
https://regex101.com/


 QUANTOREN
 ? => entweder null oder ein Zeichen
 * => entweder null oder unbegrenzt
 + => entweder 1 oder mehr
 {n} oder {n,} oder {min,max} => entweder n-zeichen oder ab n zeichen oder # min-max-Bereich

 ANCHORS
 ^ => am Anfang eines Strings
 $ => am Ende eines String
 \b => Am Anfang oder Ende eines Wortes (\B => not boundary)

 IDENTIFYER
. => irgendein Zeichen
[a-z0-9] => alle Zeichen von a - z und 0 - 9
[abc] => Menge der erlaubten Zeichen
\d => Zahl 0-9, \D=> Nicht Zahl
\w => Word a-z A-Z 0-9, \W => nicht-Wort
\s => Whitespace, \S => not-Whitespace
(ab) => Gruppe
"""

import re

# Wozu Regex? Alley Maier finden...
alle_maier = "Meyer Mauser Maier Mayer Wolf Meier Meir Major Mayr Majer"

# Verfeinerung mit Quantor {1}: mindestens ein bestimmter Buchstabe
alle_maier = "Meyer Meyyer Maiier Mayer Meier Meir Mai Major"

# Literale erkennen: "om" kommt exakt so im Text vor
m = "omikron_omikron-omaha-Gelber_tagesstern_2_7"
