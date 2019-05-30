from abc import ABC, abstractmethod
from random import randint

from WirtualnySwiat.Organizm import Organizm


class Roslina(Organizm):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)

    def akcja(self):
        """Rozprzestrzenianie roślin"""
        if randint(0, 20) == 0:
            zajete = False
            nowe_polozenie = self.losuj_polozenie()
            for org in self._swiat.get_nowe_organizmy():  # do sprawdzenia
                if nowe_polozenie == org.get_polozenie():
                    zajete = True
                    break
            if not zajete:
                self._swiat.dodaj_organizm(self._typ, nowe_polozenie)

    def kolizja(self, drugi):
        pass

    @abstractmethod
    def rysowanie(self):
        pass

