import copy

import math

from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Zwierze import Zwierze
from WirtualnySwiat.rosliny import Sosnowski


class CyberOwca(Zwierze):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 11
        self._inicjatywa = 4
        self._typ = Rodzaj.cyberowca

    def akcja(self):
        # ustalenie kierunku ruchu - tam gdzie najbliższy Barszcz Sosnowskiego
        nowe_polozenie = copy.deepcopy(self.get_polozenie())
        barszcze = [org for org in self._swiat.get_organizmy() if isinstance(org, Sosnowski.Sosnowski)]
        if barszcze:
            barszcze.sort(key=lambda org: math.sqrt((org.get_polozenie().x - self.get_polozenie().x)**2
                                                    + (org.get_polozenie().y - self.get_polozenie().y)**2))
            cel = barszcze[0]
            if cel.get_polozenie().x > self.get_polozenie().x:
                nowe_polozenie.x += 1
            elif cel.get_polozenie().x < self.get_polozenie().x:
                nowe_polozenie.x -= 1
            if cel.get_polozenie().y > self.get_polozenie().y:
                nowe_polozenie.y += 1
            elif cel.get_polozenie().y < self.get_polozenie().y:
                nowe_polozenie.y -= 1
        else:
            nowe_polozenie = self.losuj_polozenie()

        zajete = False
        for org in self._swiat.get_organizmy():
            if org.get_polozenie() == nowe_polozenie and org.get_czy_zyje() and org != self:
                zajete = True
                self.kolizja(org)
                break
        if not zajete:
            self.set_polozenie(nowe_polozenie)

    def rysowanie(self, pole):
        pole.setText("cyber-owca")
        pole.setStyleSheet("background-color: rgb(255, 100, 248);")
