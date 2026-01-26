user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001
print(type(wersja))  # <class 'float'>, liczby zmiennoprzecinkowe
liczba = 980765123456123  # int

print("Witaj %s,  masz teraz %d lat." % (user, wiek))
# %d - digit, liczba
# Witaj Tomek,  masz teraz 39 lat.

# sprawdza typy danych
# print("Witaj %d,  masz teraz %d lat." % (user, wiek))
# TypeError: %d format: a real number is required, not str

print(f"Witaj {user}, masz teraz {wiek} lat.")
# Witaj Tomek, masz teraz 39 lat.

# %i - int
# %f - float

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4, zaokrąglił
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4, zaokrąglił
print("Używamy wersji pythona %.f" % 3.5)  # Używamy wersji pythona 4, zaokrąglił

x = 3.8769
print(x)
y = round(x)
print(y)  # 4

z = round(x, 2)
print(f"{z=}")  # z=3.88
print(type(z))  # <class 'float'>

print(f"Uzywam pythona w wersji {wersja}")  # Uzywam pythona w wersji 3.90001
print(f"Uzywam pythona w wersji {wersja:.2f}")  # Uzywam pythona w wersji 3.90
print(f"Uzywam pythona w wersji {wersja:.1f}")  # Uzywam pythona w wersji 3.9
print(f"Uzywam pythona w wersji {wersja:.0f}")  # Uzywam pythona w wersji 4

print(f"{user:<10}")  # "Tomek     "
print(f"{user:>10}")  # "     Tomek"
print(f"{user:^20}")  # "       Tomek        "
print(f"{user:.^20}")  # ".......Tomek........"

print(liczba)  # 980765123456123
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 980,765,123,456,123
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 980 765 123 456 123
print(f"Nasza duża liczba {liczba:_}".replace("_", "."))  # Nasza duża liczba 980.765.123.456.123

liczba = 15_000_000_000_000
print(liczba)
print(type(liczba))
# 15000000000000
# <class 'int'>
