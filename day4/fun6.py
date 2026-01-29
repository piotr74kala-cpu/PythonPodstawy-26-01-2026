# funkcję obliczająćą średnią (ocen)
def srednia(name=None, *cyfry):  # * dowolna ilość argumentów pozycyjnych
    print(cyfry)

    count = len(cyfry)
    suma_p = sum(cyfry)

    suma = 0
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi: {avg}")
        print(f"Średnia dla ucznia {name} wynosi: {avg_p}")
    finally:
        print("Kolejny uczeń")


srednia()
srednia(1, 2)
srednia(1, 2, 3, 4)
# ()
# (1, 2)
# (1, 2, 3, 4)
# ()
# Bład: division by zero
# Kolejny uczeń
# (1, 2)
# Średnia wynosi: 1.5
# Kolejny uczeń
# (1, 2, 3, 4)
# Średnia wynosi: 2.5
# Kolejny uczeń
