"""
Aufgabe:
Gegeben ist eine Liste mit Logeinträgen aus einem kleinen Webserver.
Analysiere die Einträge mit Pattern Matching und gib passende Meldungen aus.

Fälle:
1. Wenn der Eintrag ein String ist, der mit "ERROR" beginnt:
   → Ausgabe: "Fehler erkannt: <nachricht>"
2. Wenn der Eintrag ein Dictionary mit "code" ist:
   - Wenn code >= 400 → "HTTP-Fehler <code>"
   - Sonst → "HTTP OK <code>"
3. In allen anderen Fällen:
   → Ausgabe: "Unbekannter Logeintrag"

Beispiel:
Eingabe:
["ERROR Timeout", {"code": 200}, {"code": 503}, 42]

Ausgabe:
Fehler erkannt: Timeout
HTTP OK 200
HTTP-Fehler 503
Unbekannter Logeintrag
"""

logs = ["ERROR Timeout", {"code": 200}, {"code": 503}, 42]
