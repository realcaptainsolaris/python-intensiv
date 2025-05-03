"""
Dieses Skript erklärt typische Komplexitätsprobleme bei rekursiven Funktionen
in Python – also Laufzeit- und Speicherprobleme, die bei tiefer oder
nicht optimal gesteuerter Rekursion entstehen können.

**Typische Probleme:**

1. **Exponentielles Wachstum:**
   - Wenn rekursive Aufrufe mehrfach verzweigen (z. B. naive Fibonacci-Implementierung),
     wächst die Anzahl der Aufrufe exponentiell.
   - Lösung: Zwischenspeichern mit Memoisierung oder Iteration bevorzugen.

2. **Stack Overflow / RecursionError:**
   - Python hat eine maximale Rekursionstiefe (`sys.getrecursionlimit()`),
     bei tiefer Rekursion (z. B. 10.000+ Schritte) bricht das Programm ab.
   - Lösung: Rekursionstiefe erhöhen oder iterative Umsetzung bevorzugen.

3. **Redundante Berechnungen:**
   - Ohne Caching werden gleiche Teilprobleme mehrfach gelöst.
   - Lösung: `functools.lru_cache` oder explizite Memoisierung verwenden.

4. **Ungeeignete Probleme für Rekursion:**
   - Lineare Abläufe (z. B. einfache Zählschleifen) sind mit Iteration klarer,
     effizienter und leichter zu debuggen.

Dieses Skript demonstriert problematische und effiziente Varianten


Fibonacci-Baum rekursiv:

                    fib(4)
                   /      \
              fib(3)       fib(2)
             /     \       /     \
        fib(2)   fib(1) fib(1)  fib(0)
        /    \     |      |       |
   fib(1)  fib(0)  1      1       0
     |       |
     1       0
"""

import sys
from functools import lru_cache

print("Maximale Rekursionstiefe:", sys.getrecursionlimit())


# ---------------------------------------------
# Beispiel 1: Naive Fibonacci (rekursiv, ineffizient)
# siehe Baum
# ---------------------------------------------
def fib_naiv(n):
    """Berechnet die n-te Fibonacci-Zahl rekursiv ohne Zwischenspeicherung.
    Sehr ineffizient bei großen n wegen exponentieller Aufrufanzahl."""
    if n < 2:
        return n
    return fib_naiv(n - 1) + fib_naiv(n - 2)


# ---------------------------------------------
# Beispiel 2: Fibonacci mit Memoisierung (Top-Down)
# ---------------------------------------------
@lru_cache(maxsize=None)
def fib_memo(n):
    """Rekursive Fibonacci mit Memoisierung über lru_cache.
    Wiederverwendet bereits berechnete Werte."""
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


# ---------------------------------------------
# Beispiel 3: Fibonacci mit dynamischer Programmierung (Bottom-Up)
# ---------------------------------------------
def fib_dp(n):
    """Berechnet Fibonacci-Zahl iterativ mit DP-Tabelle (Bottom-Up)."""
    if n < 2:
        return n
    dp = [0, 1]  # Startwerte für F(0) und F(1)
    for i in range(2, n + 1):
        dp.append(dp[-1] + dp[-2])  # F(n) = F(n-1) + F(n-2)
    return dp[n]


# ---------------------------------------------
# Vergleich der verschiedenen Methoden
# ---------------------------------------------
n = 40
print("Fibonacci naive:", fib_naiv(n))  # Sehr langsam ab n > 35
print("Fibonacci memo:", fib_memo(n))
print("Fibonacci DP:", fib_dp(n))

