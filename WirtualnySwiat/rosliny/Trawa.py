from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Roslina import Roslina


class Trawa(Roslina):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 0
        self._inicjatywa = 0
        self._typ = Rodzaj.trawa

    def rysowanie(self, pole):
        pole.setText("trawa")
        pole.setStyleSheet("background-color: rgb(0, 150, 20);")
