from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Roslina import Roslina


class WilczeJagody(Roslina):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 99
        self._inicjatywa = 0
        self._typ = Rodzaj.jagody

    def kolizja(self, drugi):
        drugi.set_czy_zyje(False)
        self._swiat.dodaj_komunikat(drugi.get_typ().name + " umiera od zjedzenia wilczych jagod na pozycji " +
                                    str(self.get_polozenie().x) + "," + str(self.get_polozenie().y) + ". ")

    def rysowanie(self, pole):
        pole.setText("jagody")
        pole.setStyleSheet("background-color: rgb(151, 46, 185);")
