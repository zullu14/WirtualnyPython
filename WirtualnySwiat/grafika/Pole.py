from PyQt5.QtWidgets import QLabel, QInputDialog

from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Wspolrzedne import Wspolrzedne


class Pole(QLabel):

    def __init__(self, swiat, wys, szer):
        super().__init__()
        self.__swiat = swiat
        self.__rows = wys
        self.__cols = szer

    def clear(self):
        self.setText("")
        self.setStyleSheet("background-color: rgb(195, 195, 145);")

    def mousePressEvent(self, me):
        for org in self.__swiat.get_organizmy():
            if org.get_polozenie().x == self.__rows and org.get_polozenie().y == self.__cols:
                return

        items = [typ.name for typ in Rodzaj if typ is not Rodzaj.czlowiek]

        typ, ok = QInputDialog.getItem(self, "Wybierz organizm", "Rodzaje: ", items, 0, False)

        if ok and typ:
            self.__swiat.dodaj_wlasny_organizm(typ, Wspolrzedne(self.__rows, self.__cols))
            self.__swiat.rysuj_swiat()
