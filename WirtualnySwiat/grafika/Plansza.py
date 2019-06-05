from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox

from WirtualnySwiat.grafika.Pole import Pole


class Plansza(QGroupBox):

    def __init__(self, swiat):
        super().__init__()
        self.__swiat = swiat
        self.__szer = swiat.get_cols()
        self.__wys = swiat.get_rows()
        self.__mapa = [[Pole(swiat, i, j) for j in range(self.__szer)] for i in range(self.__wys)]
        grid_layout = QGridLayout()

        for i in range(self.__wys):
            for j in range(self.__szer):
                grid_layout.addWidget(self.__mapa[i][j], i, j)
                self.__mapa[i][j].setAlignment(Qt.AlignCenter)

        self.setLayout(grid_layout)

    def rysuj_organizmy(self):
        for i in range(self.__wys):
            for j in range(self.__szer):
                self.__mapa[i][j].clear()

        for org in self.__swiat.get_organizmy():
            org.rysowanie(self.__mapa[org.get_polozenie().x][org.get_polozenie().y])