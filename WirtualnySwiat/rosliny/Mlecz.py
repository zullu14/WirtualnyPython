from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Roslina import Roslina


class Mlecz(Roslina):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 0
        self._inicjatywa = 0
        self._typ = Rodzaj.mlecz

    def akcja(self):
        super().akcja()
        super().akcja()
        super().akcja()

    def rysowanie(self, pole):
        pole.setText("mlecz")
        pole.setStyleSheet("background-color: rgb(255, 242, 0);")
