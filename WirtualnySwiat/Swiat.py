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

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def get_tura(self):
        return self.__tura

    def get_kierunek(self):
        return self.__kierunek

    def set_kierunek(self, kierunek):
        self.__kierunek = kierunek

    def get_organizmy(self):
        return self.__organizmy

    def get_nowe_organizmy(self):
        return self.__noweOrganizmy

    def get_komunikaty(self):
        return self.__komunikaty

    def wykonaj_ture(self):
        """TODO"""

    def dodaj_komunikat(self, info):
        self.__komunikaty.append(info)

    def dodaj_wlasny_organizm(self, typ, miejsce):
        org = {
            "wilk": print("wilk"),  #TODO
            "owca": print("owca"),  #TODO
            "zolw": print("zolw"),  #TODO
            "lis": print("lis")  #TODO
            #TODO
        }.get(typ, "owca")
        #self.__organizmy.append(org(self, miejsce))

    def rysuj_swiat(self):
        """TODO"""

    def zapisz_swiat(self, plik):
        """TODO"""

    def wczytaj_swiat(self, plik):
        """TODO"""

    """roboczo"""
    def __repr__(self):
        return str(self.__kierunek.value)

