from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Zwierze import Zwierze


class Wilk(Zwierze):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 9
        self._inicjatywa = 5
        self._typ = Rodzaj.wilk

    def rysowanie(self):
        print("wilk")
