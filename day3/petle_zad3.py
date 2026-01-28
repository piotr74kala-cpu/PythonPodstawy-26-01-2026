# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat")

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

licznik = 0
while True:
    licznik += 1  # spam = spam + 1
    print("Kominikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(50 * "-")
print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")

# password = input("Podaj hasło:")
# while password != 'secret':  # != - rózne
#     password = input("Podaj ponownie:")

# Podaj hasło:sasdasd
# Podaj ponownie:adaasdas
# Podaj ponownie:dsasdasdad
# Podaj ponownie:asdasdads
# Podaj ponownie:secret
#
# lista = []
# lista_int = []
# while True:
#     wej = input("Podaj liczbę:")
#     # A string is numeric if all characters in the string are numeric
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
#
# print(lista)  # ['1', '2', '3', '4', '5']#
# print(lista_int)  # [1, 2, 3, 4, 5]#

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
while 5 in my_list:
    my_list.remove(5)
print(my_list)  # [1, 2, 3, 4, 6]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}
print(list(dict.fromkeys(my_list)))
# [1, 5, 2, 3, 4, 6] - bez utraty kolejności
