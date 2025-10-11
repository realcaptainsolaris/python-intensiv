"""(MITTEL)

Es soll eine Klasse Matrix erstellt werden, die den Zugriff auf ein Element
sowie das Schreiben eines Elements in der Matrix wie folgt durchführt


# Create a 2x2 matrix
matrix = Matrix(2, 2)

# Zeile und Spalte angeben und Wert zuweisen
matrix[0, 0] = 1
matrix[0, 1] = 2
matrix[1, 0] = 3
matrix[1, 1] = 4

# Zeile und Spalte angeben und Wert auslesen
# print(matrix[0, 1])
# print(matrix[0, 3]) # Raise IndexError

# Display the matrix
print(matrix)

1 2
3 4

Hinweis: Um die Aufgabe zu lösen, muss zum Beispiel die Dunder-Methoden __setitem__
der Klasse Matrix überschrieben werden.
"""
