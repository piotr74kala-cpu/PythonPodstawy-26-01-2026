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

print(tupla_imiona.index("Radek"))  # indeks numer: 2
print(tupla_imiona.count("Radek"))  # występuje 1 raz

print(len(tupla_imiona))  # długośc 4

