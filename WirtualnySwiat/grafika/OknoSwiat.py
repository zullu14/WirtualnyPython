from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QGroupBox, QHBoxLayout, QPushButton, \
    QStackedWidget

from WirtualnySwiat.Akcje import Akcje
from WirtualnySwiat.grafika.Plansza import Plansza
from WirtualnySwiat.zwierzeta.Czlowiek import Czlowiek


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

        self.__buforowane = QStackedWidget()
        self.__buforowane.setGeometry(0, 0, self.__szer, self.__wys/2)
        self.__buforowane.setMaximumHeight(self.__wys/2)
        self.__buforowane.addWidget(self.__plansza)

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

        zapisz_b = QPushButton("Zapisz Stan", self)
        zapisz_b.setMaximumHeight(self.__wys / 10)
        zapisz_b.setMaximumWidth(self.__szer / 10)
        zapisz_b.clicked.connect(self.on_click_zapisz)
        zapisz_b.setFocusPolicy(Qt.NoFocus)

        wczytaj_b = QPushButton("Wczytaj Stan", self)
        wczytaj_b.setMaximumHeight(self.__wys / 10)
        wczytaj_b.setMaximumWidth(self.__szer / 10)
        wczytaj_b.clicked.connect(self.on_click_wczytaj)
        wczytaj_b.setFocusPolicy(Qt.NoFocus)

        panel_komunikacji = QGroupBox()
        info_layout = QHBoxLayout()
        info_layout.addWidget(self.__komunikaty)
        info_layout.addWidget(self.__sterowanie)
        panel_komunikacji.setLayout(info_layout)
        panel_komunikacji.setMaximumHeight(self.__wys/4)

        panel_przyciskow = QGroupBox()
        button_layout = QHBoxLayout()
        button_layout.addWidget(nowa_tura)
        button_layout.addWidget(zapisz_b)
        button_layout.addWidget(wczytaj_b)
        panel_przyciskow.setLayout(button_layout)
        panel_przyciskow.setMaximumHeight(self.__wys/4)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.__buforowane)
        main_layout.addWidget(panel_komunikacji)
        main_layout.addWidget(panel_przyciskow)
        self.setLayout(main_layout)

    def rysuj_organizmy(self):
        self.__plansza.rysuj_organizmy()

    def reset_planszy(self):
        self.__buforowane.removeWidget(self.__plansza)
        self.__plansza = Plansza(self.__swiat)
        self.__buforowane.addWidget(self.__plansza)

    def ustaw_komunikaty(self):
        caly_tekst = ""
        for info in self.__swiat.get_komunikaty():
            caly_tekst += info
            caly_tekst += "\n"
        self.__komunikaty.setText(caly_tekst)

    def ustaw_panel_sterowania(self, opcja=None):
        caly_tekst = ""
        caly_tekst += "Lista dostępnych akcji: \n"
        czlowiek_zyje = False
        licznik = -1
        # sprawdź czy Człowiek żyje i spisz licznik:
        for org in self.__swiat.get_organizmy():
            if isinstance(org, Czlowiek):
                czlowiek_zyje = True
                licznik = org.get_licznik_tarczy()
                break
        if czlowiek_zyje:
            caly_tekst += ">> klawisze strzałek (prawo, lewo, góra, dół) - ruch Człowieka \n"
            if licznik > 5:
                caly_tekst += "TARCZA ALZURA JEST AKTYWNA \n"
            elif licznik > 0:
                caly_tekst += ("Tarcza Alzura będzie aktywna za " + str(licznik))
                if licznik == 5:
                    caly_tekst += " tur \n"
                elif licznik == 1:
                    caly_tekst += " turę \n"
                else:
                    caly_tekst += " tury \n"
            elif licznik == 0:
                caly_tekst += ">> SPACJA - aktywacja Tarczy Alzura \n"
        else:
            caly_tekst += ">> klawisze strzalek /spacja - kolejna tura \n"

        caly_tekst += ">> dedykowane przyciski - kolejna tura, zapis, odczyt i zakończenie \n"
        caly_tekst += ">> kliknięcie myszką w puste pole - dodanie nowego organizmu z listy \n"
        if opcja is not None:
            caly_tekst += opcja
        self.__sterowanie.setText(caly_tekst)

    def on_click_nowa_tura(self):
        self.__swiat.wykonaj_ture()

    def on_click_zapisz(self):
        self.__swiat.zapisz_swiat()
        self.ustaw_panel_sterowania("Stan gry zapisany do pliku. ")

    def on_click_wczytaj(self):
        self.__swiat.wczytaj_swiat()

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

