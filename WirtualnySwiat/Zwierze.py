from abc import ABC, abstractmethod

from WirtualnySwiat.Organizm import Organizm
from WirtualnySwiat.Roslina import Roslina


class Zwierze(Organizm):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)

    def akcja(self):
        if not self.get_czy_rozmnozyl_sie():
            zajete = False
            nowe_polozenie = self.losuj_polozenie()
            if nowe_polozenie != self._polozenie:
                for org in self._swiat.get_organizmy():     # do sprawdzenia
                    if nowe_polozenie == org.get_polozenie() and org.get_czy_zyje():
                        zajete = True
                        self.kolizja(org)
                        break
                if not zajete:
                    self._polozenie = nowe_polozenie

    def kolizja(self, drugi):
        """Rozmnażanie zwierząt"""
        if self._typ == drugi.get_typ():
            self.set_czy_rozmnozyl_sie(True)
            drugi.set_czy_rozmnozyl_sie(True)
            zajete = False
            nowe_polozenie = self.losuj_polozenie()
            for org in self._swiat.get_nowe_organizmy():  # do sprawdzenia
                if nowe_polozenie == org.get_polozenie():
                    zajete = True
                    break
            if not zajete:
                self._swiat.dodaj_organizm(self._typ, nowe_polozenie)
        elif isinstance(drugi, Roslina):      # Zjadanie rośliny
            self._polozenie = drugi.get_polozenie()
            drugi.kolizja(self)
            drugi.set_czy_zyje(False)
        elif not drugi.czy_odbil_atak(self):    # Walka
            self._polozenie = drugi.get_polozenie()
            if drugi.czy_uciekl(self):
                return
            elif self._sila >= drugi.get_sila():
                self._swiat.dodaj_komunikat(self.get_typ().name + " zabija " + drugi.get_typ().name + " na pozycji " +
                                            str(self._polozenie.x) + "," + str(self._polozenie.y) + ". ")
                drugi.set_czy_zyje(False)
            else:
                self._swiat.dodaj_komunikat(drugi.get_typ().name + " zabija " + self.get_typ().name + " na pozycji " +
                                            str(self._polozenie.x) + "," + str(self._polozenie.y) + ". ")
                self.set_czy_zyje(False)

    @abstractmethod
    def rysowanie(self):
        pass
