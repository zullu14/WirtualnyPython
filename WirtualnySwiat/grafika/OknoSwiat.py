from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QGroupBox, QHBoxLayout, QPushButton

from WirtualnySwiat.Akcje import Akcje
from WirtualnySwiat.grafika.Plansza import Plansza


class OknoSwiat(QWidget):

    def __init__(self, swiat):
        super().__init__()
        self.__swiat = swiat
        self.setWindowTitle("Michał Baranowski 165463")
        self.__screen = QDesktopWidget().screenGeometry()
        self.__wys = self.__screen.height()
        self.__szer = self.__screen.width()
        self.setGeometry(0, 0, self.__szer, self.__wys)
        self.__plansza = Plansza(swiat)
        self.__plansza.setGeometry(0, 0, self.__szer, self.__wys/2)

        self.__komunikaty = QLabel()
        self.__komunikaty.setMaximumWidth(self.__szer / 2 - 100)
        self.__komunikaty.setMaximumHeight(self.__wys / 4)
        self.__komunikaty.setAlignment(Qt.AlignTop)
        self.__komunikaty.setText("roboczy tekst")
        self.__komunikaty.setWordWrap(True)

        self.__sterowanie = QLabel()
        self.__sterowanie.setMaximumWidth(self.__szer/2 - 100)
        self.__sterowanie.setMaximumHeight(self.__wys/4)
        self.__sterowanie.setAlignment(Qt.AlignTop)
        self.__sterowanie.setText("roboczy 2")
        self.__sterowanie.setWordWrap(True)

        nowa_tura = QPushButton("Nowa Tura", self)
        nowa_tura.setMaximumHeight(self.__wys/10)
        nowa_tura.setMaximumWidth(self.__szer/10)
        nowa_tura.clicked.connect(self.on_click_nowa_tura)
        nowa_tura.setFocusPolicy(Qt.NoFocus)

        panel_komunikacji = QGroupBox()
        info_layout = QHBoxLayout()
        info_layout.addWidget(self.__komunikaty)
        info_layout.addWidget(self.__sterowanie)
        panel_komunikacji.setLayout(info_layout)
        panel_komunikacji.setMaximumHeight(self.__wys/4)

        panel_przyciskow = QGroupBox()
        button_layout = QHBoxLayout()
        button_layout.addWidget(nowa_tura)
        panel_przyciskow.setLayout(button_layout)
        panel_przyciskow.setMaximumHeight(self.__wys/4)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.__plansza)
        main_layout.addWidget(panel_komunikacji)
        main_layout.addWidget(panel_przyciskow)
        self.setLayout(main_layout)

    def rysuj_organizmy(self):
        self.__plansza.rysuj_organizmy()

    def ustaw_komunikaty(self):
        caly_tekst = ""
        for info in self.__swiat.get_komunikaty():
            caly_tekst += info
            caly_tekst += "\n"
        self.__komunikaty.setText(caly_tekst)

    @pyqtSlot()
    def on_click_nowa_tura(self):
        self.__swiat.wykonaj_ture()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Up:
            self.__swiat.set_kierunek(Akcje.gora)
            self.__swiat.wykonaj_ture()
        elif event.key() == Qt.Key_Down:
            self.__swiat.set_kierunek(Akcje.dol)
            self.__swiat.wykonaj_ture()
        elif event.key() == Qt.Key_Right:
            self.__swiat.set_kierunek(Akcje.prawo)
            self.__swiat.wykonaj_ture()
        elif event.key() == Qt.Key_Left:
            self.__swiat.set_kierunek(Akcje.lewo)
            self.__swiat.wykonaj_ture()
        elif event.key() == Qt.Key_Space:
            self.__swiat.set_kierunek(Akcje.spacja)
            self.__swiat.wykonaj_ture()
        else:
            pass

