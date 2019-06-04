import sys

from PyQt5.QtWidgets import QApplication

from WirtualnySwiat.Swiat import Swiat

if __name__ == "__main__":
    app = QApplication(sys.argv)
    swiat = Swiat(12, 12)
    sys.exit(app.exec_())
