"""
Einführung in Exception Handling (Fehlerbehandlung in Python)

Beispiel ohne Fehlerbehandlung:
    x = int(input("Zahl eingeben: "))
    print(10 / x)  # Fehler, wenn x == 0 oder keine Zahl eingegeben wurde

Das Programm würde hier mit einer Fehlermeldung abbrechen.

Mit Exception Handling (try / except) kann man solche Situationen kontrolliert abfangen:

    try:
        x = int(input("Zahl eingeben: "))
        print(10 / x)
    except ValueError:
        print("Ungültige Eingabe – bitte eine Zahl eingeben.")
    except ZeroDivisionError:
        print("Division durch Null ist nicht erlaubt.")

Ablauf:
- Der Code im try-Block wird ausgeführt.
- Wenn dort ein Fehler (Exception) auftritt, springt Python in den passenden except-Block.
- Das Programm läuft danach weiter, anstatt abzustürzen.

"""
