# Zahlenratespiel
# Zufallszahl errechnen (mit random.randint), zb. 4
# maximale Rateversuche: 4
# pro Loop User Input holen. Ist user input nicht gleich der Zufallszahl
# leider falsch, bitte nochmal raten
# oder: Glück gehabt, du hast gewonnen!
# falls die Anzahl der Rateversuche >= der maximalen Rateversuche, Game over

import random

MIN = 1
MAX = 6

# Zufallszahl ziehen
number = random.randint(MIN, MAX)
