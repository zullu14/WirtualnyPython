from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Zwierze import Zwierze


class Lis(Zwierze):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 3
        self._inicjatywa = 7
        self._typ = Rodzaj.lis

    def akcja(self):
        if not self.get_czy_rozmnozyl_sie():
            zajete = False
            nowe_polozenie = self.losuj_polozenie()
            if nowe_polozenie != self._polozenie:
                """Dobry węch lisa"""
                for org in self._swiat.get_organizmy():  # do sprawdzenia
                    if nowe_polozenie == org.get_polozenie() and org.get_czy_zyje():
                        zajete = True
                        if self.get_sila() >= org.get_sila():
                            self.kolizja(org)
                        break
                if not zajete:
                    self._polozenie = nowe_polozenie

    def rysowanie(self):
        print("lis")
