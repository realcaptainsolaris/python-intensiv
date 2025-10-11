"""
Ab Python 3.10 kann anstelle des fehlenden Switch-Cases
das Structural Pattern Matching verwendet werden.
Pattern Matching ist allerdings sehr viel mächtiger als das herkömmliche
Switch-Case.

Schema:
match expression:
    case pattern1: # do something
    case pattern2: # do something else
"""

# Pattern Matching mit benutzerdefinierten Zeichenfolgen
input_string = "+ 3 3"

# Pattern Matching mit Dictionaries
orders = [
    {"type": "book", "title": "1984", "author": "George Orwell"},
    {"type": "electronics", "product": "smartphone", "brand": "Acme"},
    {"type": "grocery", "items": ["milk", "bread"], "quantities": [3, 4]},
]
