from random import randint

from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Zwierze import Zwierze


class Antylopa(Zwierze):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 4
        self._inicjatywa = 4
        self._typ = Rodzaj.antylopa

    def akcja(self):
        super().akcja()
        super().akcja()

    def kolizja(self, drugi):
        if self.get_typ() != drugi.get_typ() and isinstance(drugi, Zwierze):
            self.set_polozenie(drugi.get_polozenie())
            if self.czy_uciekl(drugi):
                return
        super().kolizja(drugi)

    def czy_uciekl(self, atakujacy):
        if randint(0, 1) == 0:
            nowe_polozenie = self.losuj_polozenie()

            if nowe_polozenie != self.get_polozenie():
                for org in self._swiat.get_organizmy():
                    if org.get_polozenie() == nowe_polozenie and org.get_czy_zyje():
                        return False
                self._swiat.dodaj_komunikat("antylopa ucieka od walki z " + atakujacy.get_typ().name +
                                            " na pozycji " + str(self.get_polozenie().x) + "," +
                                            str(self.get_polozenie().y) + ". ")
                self.set_polozenie(nowe_polozenie)
                return True
            else:
                return False
        else:
            return False

    def rysowanie(self, pole):
        pole.setText("antylopa")
        pole.setStyleSheet("background-color: rgb(228, 178, 40);")
