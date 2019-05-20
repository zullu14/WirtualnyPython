from WirtualnySwiat.Akcje import Akcje


class Swiat(object):

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__tura = 0
        self.__organizmy = []
        self.__noweOrganizmy = []
        self.__komunikaty = []
        self.__kierunek = Akcje.stoj

    """roboczo"""
    def __repr__(self):
        return str(self.__kierunek.value)

