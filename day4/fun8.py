def all_params(a, b, /, c=42, d=256):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_params(1, 2)
# a=1, b=2
# c=42, d=256
all_params(1, 2, 3, 4)
# a=1, b=2
# c=3, d=4

# / - oddziela argumenty wymagane do przekazania po pozycji
# TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'a, b'
# all_params(a=10, b=89, c=90, d=90)
all_params(67, 89, c=90, d=90)


# a=10, b=89
# c=90, d=90
# a=67, b=89
# c=90, d=90

def all_params2(name, b, /, c=42, *args, d=67, **kwargs):
    print(f"{name=}")
    print(f"{b=}")
    print(f"{c=}")
    print(f"{d=}")
    print(f"{args=}")
    print(f"{kwargs=}")


all_params2(1, 2)
all_params2(1, 2, 3)
all_params2(1, 2, c=3)
all_params2(1, 2, 3, d=90)  # musze po nazwie
all_params2(1, 2, 3, 4, 5, 6, 7, 8, d=90)  # musze po nazwie
all_params2(1, 2, 3, 4, 5, 6, 7, 8, d=90, a=10, g=90)  # musze po nazwie
# args=(4, 5, 6, 7, 8)
# kwargs={'a': 10, 'g': 90}
all_params2(1, 2, 3, 4, 5, 6, 7, 8, d=90, a=10, g=90, name="Radek")  # musze po nazwie
