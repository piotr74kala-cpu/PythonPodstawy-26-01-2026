user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001
print(type(wersja))  # <class 'float'>, liczby zmiennoprzecinkowe
liczba = 980765123456123  # int

print("Witaj %s,  masz teraz %d lat." % (user, wiek))
# %d - digit, liczba
# Witaj Tomek,  masz teraz 39 lat.

# sprawdza typy danych
print("Witaj %d,  masz teraz %d lat." % (user, wiek))
# TypeError: %d format: a real number is required, not str