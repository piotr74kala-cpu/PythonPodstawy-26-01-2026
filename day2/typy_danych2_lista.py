# kolekcje

# lista - przechowuje dowolną ilość danych, róznego typu na raz
# zachowuje kolejnośc podczas dodawania

# pusta lista
lista = []
print(type(lista))  # <class 'list'>
print(lista)  # []

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodawanie do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Piotr")
lista.append("Zenek")
lista.append("Anna")
lista.append("Magda")

print(lista)  # ['Radek', 'Tomek', 'Piotr', 'Zenek', 'Anna', 'Magda']

print(len(lista))  # 6 elementów
# ['Radek', 'Tomek', 'Piotr', 'Zenek', 'Anna', 'Magda']
#      0       1         2        3       4        5

print(lista[2])  # Piotr
print(lista[4])  # Anna

# print(lista[10])  # IndexError: list index out of range

print(lista[5])  # Magda
print(lista[len(lista) - 1])  # Magda
print(lista[-1])  # ostatni element, Magda
print(lista[-2])  # Anna
# ['Radek', 'Tomek', 'Piotr', 'Zenek', 'Anna', 'Magda']
#      0       1         2        3       4        5
#      -6       -5       -4       -3       -2      -1
