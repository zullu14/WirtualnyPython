from abc import ABC, abstractmethod
from random import randint

from WirtualnySwiat.Wspolrzedne import Wspolrzedne


class Organizm(ABC):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__()
        self._swiat = srodowisko
        self._polozenie = miejsce
        self._czyZyje = True
        self._czyRozmnozylSie = False
        if wiek is None:
            self._wiek = self._swiat.get_tura()
        else:
            self._wiek = wiek
        self._sila = sila
        self._inicjatywa = None        # do nadpisania
        self._typ = None               # do nadpisania

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
        return self._sila

    def zwieksz_sile_o(self, wartosc):
        self._sila += wartosc

    def get_inicjatywa(self):
        return self._inicjatywa

    def get_wiek(self):
        return self._wiek

    def get_polozenie(self):
        return self._polozenie

    def set_polozenie(self, nowe):
        self._polozenie = nowe

    def get_typ(self):
        return self._typ

    def get_czy_zyje(self):
        return self._czyZyje

    def set_czy_zyje(self, stan):
        self._czyZyje = stan

    def get_czy_rozmnozyl_sie(self):
        return self._czyRozmnozylSie

    def set_czy_rozmnozyl_sie(self, stan):
        self._czyRozmnozylSie = stan

    def czy_odbil_atak(self, atakujacy):
        return False

    def czy_uciekl(self, atakujacy):
        return False

    def losuj_polozenie(self):
        x_new = self._polozenie.x
        y_new = self._polozenie.y
        r = randint(0, 8)
        if r == 0:
            if self._polozenie.x > 0 and self._polozenie.y > 0:
                x_new -= 1
                y_new -= 1
        elif r == 1:
            if self._polozenie.x > 0:
                x_new -= 1
        elif r == 2:
            if self._polozenie.x > 0 and self._polozenie.y < self._swiat.get_cols() - 1:
                x_new -= 1
                y_new += 1
        elif r == 3:
            if self._polozenie.y > 0:
                y_new -= 1
        elif r == 4:
            if self._polozenie.y < self._swiat.get_cols() - 1:
                y_new += 1
        elif r == 5:
            if self._polozenie.x < self._swiat.get_rows() - 1 and self._polozenie.y > 0:
                x_new += 1
                y_new -= 1
        elif r == 6:
            if self._polozenie.x < self._swiat.get_rows() - 1:
                x_new += 1
        elif r == 7:
            if self._polozenie.x < self._swiat.get_rows() - 1 and self._polozenie.y < self._swiat.get_cols() - 1:
                x_new += 1
                y_new += 1
        else:
            if self._polozenie.x > 0 and self._polozenie.y > 0:
                x_new -= 1
                y_new -= 1

        return Wspolrzedne(x_new, y_new)
