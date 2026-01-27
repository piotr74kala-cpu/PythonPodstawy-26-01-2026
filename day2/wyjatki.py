# wyjątki - błedy podczas wykonywania programu

# print(5 / 0)
# C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\.venv\Scripts\python.exe C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\day2\wyjatki.py
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy-26-01-2026\day2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1
print("Dalsza część programu")

try:
    # print(5 / 0)
    # int("A")
    # print("A" * "23")
    # raise KeyError  # rzucenie wyjątku
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bład wartości")
except TypeError:
    print("Bład typu")
except Exception as e:
    print("Bład:", e)
else:  # gdy nie ma błędu
    print("Wynik:", wynik)
finally:  # wykonuje się zawsze
    print("Kolejne obliczenia")

print("Dalsza część programu")
# try - except - [else - finally]
# Dalsza część programu
# Wynik: 30.0
# Kolejne obliczenia
# Dalsza część programu
