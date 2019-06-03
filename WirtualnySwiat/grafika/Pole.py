from PyQt5.QtWidgets import QLabel


class Pole(QLabel):

    def __init__(self):
        super().__init__()

    def clear(self):
        self.setText("")
        self.setStyleSheet("background-color: rgb(195, 195, 145);")