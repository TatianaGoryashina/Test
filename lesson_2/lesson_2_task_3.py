import math


def square(side):
    if isinstance(side, int):
        return side * side
    else:
        return math.ceil(side * side)


# Примеры использования:
print(square(5))     # Вывод: 25
print(square(5.5))   # Вывод: 31
print(square(3.2))   # Вывод: 11
