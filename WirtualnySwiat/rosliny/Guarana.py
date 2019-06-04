from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Roslina import Roslina


class Guarana(Roslina):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 0
        self._inicjatywa = 0
        self._typ = Rodzaj.guarana

    def kolizja(self, drugi):
        drugi.zwieksz_sile_o(3)
        self._swiat.dodaj_komunikat(drugi.get_typ().name + " zjada guarane na pozycji "
                                    + str(self.get_polozenie().x) + "," + str(self.get_polozenie().y)
                                    + " i zwieksza sile o 3. ")

    def rysowanie(self, pole):
        pole.setText("guarana")
        pole.setStyleSheet("background-color: rgb(241, 55, 16);")