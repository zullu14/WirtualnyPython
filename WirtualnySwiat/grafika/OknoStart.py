from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog, QDesktopWidget, QLineEdit, QFormLayout, QPushButton, QWidget

from WirtualnySwiat.Swiat import Swiat


class OknoStart(QDialog):

    def __init__(self):
        super().__init__()
        self.__screen = QDesktopWidget().screenGeometry()
        self.__wys = self.__screen.height()/6
        self.__szer = self.__screen.width()/3
        self.setGeometry(self.__screen.width()/2 - self.__szer/2, self.__screen.height()/2 - self.__wys/2,
                         self.__szer, self.__wys)
        self.setWindowTitle("Podaj wymiary świata: ")
        self.e1 = QLineEdit()
        self.e1.setValidator(QIntValidator())
        self.e1.setMaxLength(2)

        self.e2 = QLineEdit()
        self.e2.setValidator(QIntValidator())
        self.e2.setMaxLength(2)

        ok = QPushButton("OK", self)
        ok.setMaximumWidth(self.__szer / 5)
        ok.clicked.connect(self.ok_click)

        flo = QFormLayout()
        flo.addRow("Szerokość: ", self.e1)
        flo.addRow("Wysokość: ", self.e2)
        flo.addWidget(ok)

        self.setLayout(flo)
        self.show()

    def ok_click(self):
        cols = int(self.e1.text())
        rows = int(self.e2.text())

        if cols > 1 and rows > 1:
            Swiat(rows, cols)
        else:
            print("Nie udało sie utworzyć świata o podanych wymiarach!")
        self.close()