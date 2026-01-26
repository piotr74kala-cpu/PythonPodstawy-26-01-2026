tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\.venv\Scripts\python.exe C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\day1\teskty.py
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
""" Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
# 13:50

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie

# Witaj Świecie
# 01234567890..
print(tekst[2])  # t, indeks numer 2, pozycja 3

print(tekst.index("Ś"))  # indeks numer 6

print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("w"))  # występuje 1 raz
print(tekst.lower().count("w"))  # występuje 2 razy

print(tekst.count("j", 0, 4))  # występuje 0 razy, z prawej zbiór otwarty

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie biłaych znaków, wiodących i kończących (spacji)
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
# \xc5\x9a - kod litery w systemie szesnastkowym
# \x dane w systemie szesnaastkowym
print(type(encode_s))  # <class 'bytes'>
print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
print(len(imie))  # długość tekstu 5
# f - string, sformatowany string, wstrzykiwanie zmiennych do tekstu
tekst_format = f"Mam na imię {imie}."
print(tekst_format)  # Mam na imię Radek.

tekst_format = "\tMam na imię {imie}\n i lubię Pythona.\b"
print(tekst_format)
# "	Mam na imię {imie}
#  i lubię Pythona"
# \t tabulator
# \n nowa linia
# \b backspace

starszy = "Witaj %s!"  # %s - string
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format("Raaadek"))  # Witaj Raaadek!

print("Witaj", imie)  # Witaj Radek

print("""Tekst
    wielolinijkowy""")

# "Tekst
#     wielolinijkowy"

# komentarz traktowany jako dokumentacja
"""Komentarz
 wielolinijkowy"""
