import math
from itertools import zip_longest

print(math.pi)  # 3.141592653589793
print(math.sqrt(25))  # 5.0

print(len(str(math.pi)))  # 17

angle_degree = 30
angle_radians = math.radians(angle_degree)
print(angle_radians)  # 0.5235987755982988

sin_val = math.sin(angle_radians)
print(f"sin({angle_degree}) = {sin_val}")
# sin(30) = 0.49999999999999994

angles = [0, 30, 45, 60, 90]

sin_values = [math.sin(math.radians(a)) for a in angles]

for a, s in zip(angles, sin_values):
    print(f"sin({a}) = {s:.2f}")
# sin(0) = 0.00
# sin(30) = 0.50
# sin(45) = 0.71
# sin(60) = 0.87
# sin(90) = 1.00

imiona = ["Radek", "Tomek", 'Agata', "Marek", "Magda"]
wiek = [44, 56, 23, 38]

zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x0000028B98790F90>

# for item in zipped:
#     print(item)
# ('Radek', 44)
# ('Tomek', 56)
# ('Agata', 23)
# ('Marek', 38)
# ('Magda', None)
# iterator nie trzyma danych - zwykle można skorzystać tylko raz
print(40 * "-")
for o, w in zipped:
    print(o, w)
# ----------------------------------------
# Radek 44
# Tomek 56
# Agata 23
# Marek 38
# Magda None
