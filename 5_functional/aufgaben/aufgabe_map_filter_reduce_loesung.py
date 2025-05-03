from functools import reduce
from operator import add

people = [
    {"name": "Foo", "height": 160},
    {"name": "Bar", "height": 180},
    {"name": "Baz", "height": 80},
    {"name": "Grumpy", "height": 80},
    {"name": "Waldo"},
]

heights = list(
    map(lambda x: x["height"],
        filter(lambda x: "height" in x, people))
)
result = reduce(add, heights, 0)
if heights:
    print(result / len(heights))
else:
    print("Kein Ergebnis.")
