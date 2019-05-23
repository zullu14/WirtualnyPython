from abc import ABC, abstractmethod


class Organizm(ABC):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__()
        self.__swiat = srodowisko
        self.__polozenie = miejsce
        self.__czyZyje = True
        self.__czyRozmnozylSie = False
        if wiek is None:
            self.__wiek = self.__swiat.get_tura()
        else:
            self.__wiek = wiek
        self.__sila = sila
        self.__inicjatywa = None        # do nadpisania
        self.__typ = None               # do nadpisania

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, drugi):
        pass

    @abstractmethod
    def rysowanie(self):
        pass

    def get_sila(self):
        return self.__sila

    def zwieksz_sile_o(self, wartosc):
        self.__sila += wartosc

    def get_inicjatywa(self):
        return self.__inicjatywa

    def get_wiek(self):
        return self.__wiek

    def get_polozenie(self):
        return self.__polozenie

    def set_polozenie(self, nowe):
        self.__polozenie = nowe

    def get_typ(self):
        return self.__typ

    def get_czy_zyje(self):
        return self.__czyZyje

    def set_czy_zyje(self, stan):
        self.__czyZyje = stan

    def get_czy_rozmnozyl_sie(self):
        return self.__czyRozmnozylSie

    def set_czy_rozmnozyl_sie(self, stan):
        self.__czyRozmnozylSie = stan

    def czy_odbil_atak(self, atakujacy):
        return False

    def czy_uciekl(self, atakujacy):
        return False

    def losuj_polozenie(self):
        """TODO"""