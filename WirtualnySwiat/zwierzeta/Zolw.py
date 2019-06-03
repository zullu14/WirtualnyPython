from random import randint

from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Zwierze import Zwierze


class Zolw(Zwierze):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 2
        self._inicjatywa = 1
        self._typ = Rodzaj.zolw

    def akcja(self):
        if randint(0, 3) == 0:
            super().akcja()

    def czy_odbil_atak(self, atakujacy):
        if atakujacy.get_sila() < 5:
            self._swiat.dodaj_komunikat("zolw odbil atak " + atakujacy.get_typ().name + " na pozycji " +
                                        str(self.get_polozenie().x) + "," + str(self.get_polozenie().y) + ". ")
            return True
        else:
            return False

    def rysowanie(self, pole):
        pole.setText("zolw")
        pole.setStyleSheet("background-color: rgb(185, 140, 17);")
