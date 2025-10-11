"""
Aufgabe: Charaktere für ein Roleplaying Game (schwer)

Definiere eine abstrakte Basisklasse `Character` für Rollenspielcharaktere.
Diese Basisklasse enthält zwei abstrakte Methoden, `attack` und `heal`, die von
abgeleiteten Klassen implementiert werden müssen. Attack und Heal erwarten
einen anderen Character als Argument. Ein Charakter hat einen Namen und eine
Gesundheit (Health), die beim Instanziieren festgelegt wird.

Jede abstrakte Methode ist mit einem Docstring versehen, der erklärt, wofür sie
verwendet wird und welche Argumente sie erwartet. Die Parameter werden mit
Datentypen versehen.

- Es gibt zwei konkrete Klassen, `Warrior` (Krieger) und `Healer` (Heiler), die
  von der abstrakten Basisklasse `Character` erben. Jede dieser Klassen
  implementiert die abstrakten Methoden `attack` und `heal` auf ihre eigene
  Weise.

- Erstelle Instanzen von Krieger und Heiler und demonstrieren deren
  Fähigkeiten, indem wir die `attack`- und `heal`-Methoden aufrufen. Das
  Ergebnis jeder Aktion kann einfach als print() ausgegeben werden.

warrior = Warrior("Boromir", health=100)
healer = Healer("Gandalf", health=80)

warrior.attack(healer, damage=10)  # Krieger greift Heiler an und fügt 10 Schaden zu.
healer.heal(warrior, value=15)    # Heiler heilt Krieger um 15 Gesundheitspunkte.

warrior.heal(healer, value=15)    # ERROR! Ein Krieger hat keine Heilkräfte!
warrior.attack(warrior, damage=10)  # ERROR! Ein Spieler kann sich nicht selbst angreifen

healer.heal(healer, value=15) # Heiler heilt Heiler um 15: Gesundsheitspunkte
"""

from __future__ import annotations
from abc import ABC, abstractmethod
