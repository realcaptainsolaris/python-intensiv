"""
math_demo.py

Demonstration zentraler Funktionen des Python-Moduls `math`.

Dieses Skript zeigt Beispielausgaben folgender Operationen:

1. Betrag (fabs)
2. Quadratwurzel (sqrt)
3. Potenz (pow)
4. Abrunden (floor)
5. Aufrunden (ceil)
6. Trigonometrische Funktionen: sin, cos, tan
7. Logarithmus (natürlich und Basis 10)
"""

import math

print("1. Betrag (fabs):", math.fabs(-5.3))
print("2. Quadratwurzel (sqrt):", math.sqrt(9))
print("3. Potenz (pow):", math.pow(2, 3))
print("4. Abrunden (floor):", math.floor(3.7))
print("5. Aufrunden (ceil):", math.ceil(3.7))
print("6. Sinus (sin π/2):", math.sin(math.pi / 2))
print("7. Cosinus (cos π):", math.cos(math.pi))
print("8. Tangens (tan π/4):", math.tan(math.pi / 4))
print("9. Natürlicher Logarithmus (log e):", math.log(math.e))
print("10. Logarithmus Basis 10 (log10 100):", math.log10(100))
