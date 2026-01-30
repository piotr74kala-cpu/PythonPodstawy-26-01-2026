class Human:
    """
    Klasa Human opisujaca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda  inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec
        # wypisz_wiek(), wypisz_wzrost()

    def powitanie(self):
        print(f"Nazywam się: {self.imie}")
        # print(f"Nazywam się: {cz1.imie}")

    def ruszaj(self):

        if self.plec == "m":
            print("Ruszył-em w drogę")
        else:
            print("Ruszył-am w drogę")

    # metoda opisowa
    def __str__(self):
        return f"{self.imie}, {self.wiek}, {self.wzrost}"


# TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
# cz1 = Human()

cz1 = Human("Radek", 45, 195, "m")
print(cz1.imie)
print(cz1.wzrost)
print(cz1.wiek)
print(cz1.plec)
# Radek
# 195
# 45
# m

cz1.powitanie()
cz1.ruszaj()
# Nazywam się: Radek
# Ruszył-em w drogę

cz2 = Human("Anna", 45, 167)
print(cz2.imie)

print(cz1)  # <__main__.Human object at 0x0000022ED43757F0>
# po nadpisaniu __str__
# Radek, 45, 195
