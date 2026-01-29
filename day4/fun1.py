# funkcja - wydzielony fragment kodu, można użyć w dowolnym momencie
# funkcja musi najpierw zostać zadeklarowana
# żeby uruchomić funkcję trzeba ją wywołać

a = 6
b = 8


# funkcje nie zwracają wyniku

# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # argumenty obowiązkowe
    print(a + b)


# ominięcie problemu przeciążania funkcji liczbą argumentów
# c=0  - argument o wartości domyślnej
def odejmij(a, b, c=0):
    print(a - b - c)


# wywołanie funkcji
dodaj()  # 14

# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(7, 78)  # 85

# argumenty po pozycji
odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4

# argumenty po nazwie (keywords)
odejmij(b=90, a=87)
odejmij(b=90, c=89, a=54)  # -125
dodaj2(b=8, a=90)  # 98

# mieszane
odejmij(1, 2, c=78)  # -79
dodaj2(b=8, a=90)  # 98
dodaj2(1, b=87)  # 88

# argumenty pozycyjne muszą byc przed nazwanymi
# odejmij(a=8, 1, 2)
# SyntaxError: positional argument follows keyword argument

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(dodaj() + dodaj2(5, 9))