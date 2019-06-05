import sys

from PyQt5.QtWidgets import QApplication

from WirtualnySwiat.grafika.OknoStart import OknoStart

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = OknoStart()
    sys.exit(app.exec_())
