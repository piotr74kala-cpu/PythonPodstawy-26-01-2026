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

    @abstractmethod # dekorator, metoda abstrakcyjna
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
