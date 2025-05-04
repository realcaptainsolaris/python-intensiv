"""
Tic Tac Toe - Feld Analyse

Spieler X hat begonnen.

Gegeben ist eine 3x3 Matrix, die das Spielfeld repräsentiert.
Das Spielfeld ist gefüllt mit den zwei Farben der Spieler, also X und O sowie den leeren Feldern NONE.

Aufgabe:
-------------
Wir wollen in dieser Aufgabe einige Funktionen implementieren, die das Spielfeld überprüfen. Dazu gehört neben der fachlich richtigen
Implementierung auch das Angeben der Datentypen (Type-Hints)

Wir gehen zu jeder Zeit von einem gültigen Spielfeld aus (zwei sieg-
reiche Spieler kann es zum Beispiel nicht geben)

0) Das Spielfeld:

board = [
        [X, X, O],
        [O, _, X],
        [O, X, _]
    ]

An den Feldern X und O haben die Spieler bereits gesetzt, die beiden _-Felder
sind noch ungenutzt.

Die Funktionen sollen ordentlich mit Type-Hints, Rückgabewerten und Doc-Strings beschrieben werden.

Folgende Funktionen sind zu implementieren:

------------------------------------------------------------------------------
1) player()

Welcher Spieler ist als nächstes am Zug? Wir gehen davon aus, dass
immer Spieler mit der Farbe X das Spiel begonnen hat. Implementiere diese
Funktion so, dass der aktuelle Spielstand erkannt und der nächste
Spieler berechnet wird.

Beispiel:

board = [
    [X, O, _],
    [_, _, _],
    [_, _, _]
]
Spieler X darf den nächsten Zug ausführen.


------------------------------------------------------------------------------
2) actions()
Erzeuge ein Set von allen freien Feldern der Matrix. in Form von Tupeln, die
Reihe und Spalte angegeben. Beispiel:

board = [
    [X, X, O],
    [O, _, _],
    [O, X, _]
]

Result: set{(1, 1), (1, 2), {2, 2}}

------------------------------------------------------------------------------

3) winner()

Prüft, ob es einen Gewinner gibt.
Gewinner ist die Farbe, der drei Steine in einer Reihe hat: Horizontal, Vertikal
oder diagonal

board = [
    [X, O, O],
    [X, _, _],
    [X, _, _]
]

X hat gewonnen. X wird zurückgegeben.

4) terminal()

Prüft, ob sich das Board im Endzustand befindet. Entweder,
winner() ist True
oder das Board voll belegt ist und keine Züge mehr möglich sind.

board = [
    [X, O, O],
    [X, _, _],
    [X, _, _]
]

Gibt true zurück, weil winner() True ist (X)

board = [
    [X, O, _],
    [_, _, _],
    [_, _, _]
]

gibt False zurück, weil weder winner() True noch Board voll.

"""

X = "X"
O = "O"
_ = None


def player(board: list) -> str:
    """Returns player who has the next turn on board.

    if actions count is odd, next player is O, because X player started
    the game. Return str (X or O)
    """
    pass


def actions(board: list) -> set:
    """Returns set of all possible actions.

    Args:
        Board

    Returns:
        (set): tuple with all available actions on the board. Empty set, if board is full
    """
    pass


def winner(board: list) -> str | None:
    """
    Return winner, falls existiert. Prüfe dazu alle Spalten, Reihen und die zwei
    Hauptdiagonalen. Ansonsten return None

    """
    pass


def terminal(board: list) -> bool:
    """
    gibt True zurück, wenn a) das Board voll ist oder b) ein gewinner existiert.
    (Prüft das Ergebnis von Funktion winner())

    if winner():
        return True

    Ansonsten return False
    """


if __name__ == "__main__":
    board = [
        [X, X, O],
        [O, _, X],
        [O, X, _],
    ]

    player(board)  # welcher Spiele ist als nächstes am Zug?
    actions(board)  # gib mir eine Liste aller möglichen Spielzüge
    winner(board)  # gibt es einen Gewinner? Wer ist es?
    terminal(board)  # ist das Spiel zu Ende, weil Gewinner oder alles voll?
