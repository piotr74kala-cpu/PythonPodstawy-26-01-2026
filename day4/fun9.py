# funkcja lambda
# skrócony zapis funkcji
# lambda zwraca wynik (return)
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(10, 8))  # 2

odejmij2 = lambda a, b: a - b  # domyslnie ma return
print(odejmij2(10, 2))  # 8

# oblicz_vat na lambdę
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(29))  # dorosły

# mapowanie danych
lista = [1, 2, 14, 24, 50, 67, 80, 100, 200, 500]

# stworzyc liste. do listy zapisać elementy tej listy  wykonując na nich operacje * 2

l1 = []
for i in lista:
    l1.append(i * 2)
print(l1)

print([i * 2 for i in lista])


# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)

# funkcje wyższego rzędu, jako argument przyjmuja inną funkcję
# map() - wykonuje funkcje na elementach kolekcji

print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# lambda jako funkcja anonimowa
# może być uzyta w miejscu deklaracji
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 5, lista))}")
# Zastosowanie map(): [5, 10, 70, 120, 250, 335, 400, 500, 1000, 2500]

# filtrowanie danych
l4 = []
for i in lista:
    if i < 3:
        l4.append(i)

print(l4)  # [1, 2]

# filter() - zwraca elementy spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter(): [1, 2]
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 50, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 30, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 150, lista))}")
# Zastosowanie filter(): [1, 2]
# Zastosowanie filter(): [1, 2, 14, 24]
# Zastosowanie filter(): [50, 67, 80, 100, 200, 500]
# Zastosowanie filter(): [1, 2, 14, 24, 50, 67, 80, 100]

# wieksze od 3 i mniejsze od 150
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 150, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 150, lista))}")
# Zastosowanie filter(): [14, 24, 50, 67, 80, 100]
# Zastosowanie filter(): [14, 24, 50, 67, 80, 100]
