from abc import ABC, abstractmethod


# klasa abstrakcyjna, posiada metodę abstrakcyjną
class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc, "km/h")

    @abstractmethod  # dekorator, metoda abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Kalsa Kura
    Dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # musi byc uzyte super()

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("ko ko ko koko")


class Orzel(Ptak):
    """
    Klasa dziedziczy po klasie Orzeł
    """

    # musimy nadpisac metode abstrakcyjną
    def wydaj_odglos(self):
        print("Kir kier kir kier")


class Sowa(Ptak):
    """
    Klasa Sowa
    """


# klasa abstrakcyjna
# nie można tworzyć obiektów tej klasy
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak('Orzeł', 50)
# or1.latam()  # Tu Orzeł Lecę z szybkością 50 km/h
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0 km/h

kur2 = Kura("Kura zielononóżka")
kur2.latam()  # Tu Kura zielononóżka Ja nie latam
kur2.wydaj_odglos()  # ko ko ko koko

or2 = Orzel("Orzel Bielik", 55)
or2.latam()
or2.wydaj_odglos()
# Tu Orzel Bielik Lecę z szybkością 55 km/h
# Kir kier kir kier

# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# nie ma metody wydaj_odglos
# nie można stworzyc obiektu tej klasy
# sowa = Sowa("Sowa", 15)

lista = [or2, kur2]  # obiekty różnych klas
# polimorfizm
# obiekty różnych klas maja poprzez wspólna kalsę abstrakcyjną wspolne cechy, metody

for i in lista:
    i.wydaj_odglos()
    print(i.__class__.__name__)
# Kir kier kir kier
# ko ko ko koko
# Kir kier kir kier
# Orzel
# ko ko ko koko
# Kura
# ctrl alt l - formatowanie kodu
