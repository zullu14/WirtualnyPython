from WirtualnySwiat.Akcje import Akcje
from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Zwierze import Zwierze


class Czlowiek(Zwierze):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None, licznik=0):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 5
        self._inicjatywa = 4
        self._typ = Rodzaj.czlowiek
        self._licznik_tarczy = licznik

    def get_licznik_tarczy(self):
        return self._licznik_tarczy

    def akcja(self):
        if self._licznik_tarczy > 0:
            self._licznik_tarczy -= 1
        zajete = False
        nowe_polozenie = self.get_polozenie()
        kierunek = self._swiat.get_kierunek()

        if kierunek is Akcje.prawo:
            if nowe_polozenie.y < self._swiat.get_cols() - 1:
                nowe_polozenie.y += 1
        elif kierunek is Akcje.lewo:
            if nowe_polozenie.y > 0:
                nowe_polozenie.y -= 1
        elif kierunek is Akcje.gora:
            if nowe_polozenie.x > 0:
                nowe_polozenie.x -= 1
        elif kierunek is Akcje.dol:
            if nowe_polozenie.x < self._swiat.get_rows() - 1:
                nowe_polozenie.x += 1
        elif kierunek is Akcje.spacja:
            if self._licznik_tarczy == 0:
                self._licznik_tarczy = 10
                self._swiat.dodaj_komunikat("Czlowiek aktywuje Tarcze Alzura na czas 5 tur. ")

        for org in self._swiat.get_organizmy():
            if org.get_polozenie() == nowe_polozenie and org.get_czy_zyje() and org != self:
                zajete = True
                self.kolizja(org)
                break
        if not zajete:
            self.set_polozenie(nowe_polozenie)

    def czy_odbil_atak(self, atakujacy):
        if self._licznik_tarczy > 5:
            self._swiat.dodaj_komunikat("Czlowiek odbil atak " + atakujacy.get_typ().name +
                                        " na pozycji " + str(self.get_polozenie().x) + "," + str(self.get_polozenie().y)
                                        + ". ")
            return True
        else:
            return False

    def rysowanie(self, pole):
        pole.setText("Czlowiek")
        pole.setStyleSheet("background-color: rgb(0, 222, 168);")

    def zapisz_organizm(self):
        s = self.get_typ().name + " " + str(self._polozenie.x) + " " + str(self._polozenie.y) + " "\
            + str(self._sila) + " " + str(self._wiek) + " " + str(self._licznik_tarczy)
        return s
