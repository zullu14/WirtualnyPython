from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Zwierze import Zwierze


class Owca(Zwierze):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 4
        self._inicjatywa = 4
        self._typ = Rodzaj.owca

    def rysowanie(self, pole):
        pole.setText("owca")
        pole.setStyleSheet("background-color: rgb(200, 200, 200);")
