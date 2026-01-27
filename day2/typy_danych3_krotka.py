# krotka (tupla) - lista tylko do odczytu, niemutowalna
# pozwala efektywniej zarządzać pamięcią
# krotka jedoelementowa, stała, szczególny  przypadek zmienna

tupla_imiona = "Zenek", "MArek", "Radek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'MArek', 'Radek', 'Ania')

# tupla_liczby = 43, 55, 22.34, 11, 200
tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

# tupla jedoelementowa
tupla_jeden = 45,
print(tupla_jeden)  # (45,)
print(type(tupla_jeden))  # <class 'tuple'>

# PEP8 przy tworzeniu tupli jednoelemntowych zaleca dodawanie ()
tupla_jeden = (45,)
print(tupla_jeden)  # (45,)
print(type(tupla_jeden))

# tupla jest niemutowalna
# tupla_jeden[0] = 123 # TypeError: 'tuple' object does not support item assignment

# usunięcie całęj tupli
del tupla_jeden
# print(tupla_jeden)  # NameError: name 'tupla_jeden' is not defined

# ('Zenek', 'MArek', 'Radek', 'Ania')
print(tupla_imiona.index("Radek"))  # indeks numer: 2
print(tupla_imiona.count("Radek"))  # występuje 1 raz

print(len(tupla_imiona))  # długośc 4

tup = 1, 2
print(type(tup))  # <class 'tuple'>

# a - pierwsza wartosc, b - druga wartość
a = tup[0]
b = tup[1]
print(a, b)  # 1 2

# rozpakowanie krotki
a, b = 1, 2
print(a, b)  # 1 2

a, b = tup
print(a, b)  # 1 2

print(tupla_imiona)  # ('Zenek', 'MArek', 'Radek', 'Ania')
print(len(tupla_imiona))  # 4
# name1, name2, name3
# ValueError: too many values to unpack (expected 3, got 4)
# name1, name2, name3 = tupla_imiona
name1, name2, *name3 = tupla_imiona  # * worek na pozostałę dane
print(name1, name2, name3)  # Zenek MArek ['Radek', 'Ania']
print(name1, name2, *name3)  # Zenek MArek Radek Ania - rozpakowało kolekcję

name1, *name2, name3 = tupla_imiona  # * worek na pozostałę dane
print(name1, name2, name3)  # Zenek ['MArek', 'Radek'] Ania

*name1, name2, name3 = tupla_imiona  # * worek na pozostałę dane
print(name1, name2, name3)  # Zenek ['MArek', 'Radek'] Ania

# sortowanie sorted() - zwraca posortowaną listę!!!
print(sorted(tupla_imiona))
# ['Ania', 'MArek', 'Radek', 'Zenek']

sortowana = sorted(tupla_imiona)
print(id(sortowana))
print(id(tupla_imiona))
# 2318260656384
# 2318266518640
# tupla imiona nie została zmieniona (jest niemutowalna)
print(tupla_imiona)  # ('Zenek', 'MArek', 'Radek', 'Ania')
