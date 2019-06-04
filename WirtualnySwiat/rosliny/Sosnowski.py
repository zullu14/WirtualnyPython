from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Roslina import Roslina
from WirtualnySwiat.zwierzeta import CyberOwca


class Sosnowski(Roslina):

    def __init__(self, srodowisko, miejsce, sila=None, wiek=None):
        super().__init__(srodowisko, miejsce, sila, wiek)
        if sila is None:
            self._sila = 10
        self._inicjatywa = 0
        self._typ = Rodzaj.barszcz

    def akcja(self):
        for org in self._swiat.get_organizmy():
            if (self.get_polozenie().x - 2 < org.get_polozenie().x < self.get_polozenie().x + 2
                    and self.get_polozenie().y - 2 < org.get_polozenie().y < self.get_polozenie().y + 2
                    and org.get_czy_zyje() and org != self and not isinstance(org, CyberOwca.CyberOwca)):
                org.set_czy_zyje(False)
                self._swiat.dodaj_komunikat(org.get_typ().name +
                                            " zostaje zabity przez barszcz Sosnowskiego na pozycji " +
                                            str(org.get_polozenie().x) + "," + str(org.get_polozenie().y) + ". ")

    def kolizja(self, drugi):
        if not isinstance(drugi, CyberOwca.CyberOwca):
            drugi.set_czy_zyje(False)
            self._swiat.dodaj_komunikat(drugi.get_typ().name + " umiera od zjedzenia barszczu Sosnowskiego na pozycji "
                                        + str(self.get_polozenie().x) + "," + str(self.get_polozenie().y) + ". ")
        else:
            self._swiat.dodaj_komunikat(drugi.get_typ().name + " zjada barszcz Sosnowskiego na pozycji "
                                        + str(self.get_polozenie().x) + "," + str(self.get_polozenie().y) + ". ")

    def rysowanie(self, pole):
        pole.setText("barszcz")
        pole.setStyleSheet("background-color: rgb(132, 224, 109);")
