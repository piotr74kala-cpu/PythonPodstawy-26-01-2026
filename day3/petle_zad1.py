# pętla  - możliwość wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rób

for _ in range(15):  # niema zmienna
    print("Test podłoga")
    print(_)  # można odczytać wartość

for i in range(5):
    print(i + 2)
    print(i * 2)

# przerobić lotto na pętle
# zapisac wynik do listy

lista_kule = list(range(1, 50))  # od 1 do 49
lista_wynik = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    print(wyn)
    lista_kule.remove(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)
# [28, 36, 40, 42, 14, 5]
