from WirtualnySwiat.Akcje import Akcje
from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.zwierzeta.Lis import Lis
from WirtualnySwiat.zwierzeta.Owca import Owca
from WirtualnySwiat.zwierzeta.Wilk import Wilk
from WirtualnySwiat.zwierzeta.Zolw import Zolw


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

    def stworz_swiat(self):
        # TODO
        pass

    def wykonaj_ture(self):
        self.__organizmy.sort(key=lambda org: org.get_wiek())
        self.__organizmy.sort(key=lambda org: org.get_inicjatywa(), reverse=True)
        # wyzeruj flagę czy rozmnożył się
        for org in self.__organizmy:
            org.set_czy_rozmnozyl_sie(False)
        # po kolei wykonaj akcje
        for org in self.__organizmy:
            if org.get_czy_zyje():
                org.akcja()
        # następnie usuń z listy organizmów wszystkie nieżywe
        self.usun_organizmy()

        # następnie dodaj do listy organizmów wszystkie nowo narodzone
        # TODO: dodaj nowe organizmy

        # narysuj obecny stan świata wraz z komunikatami
        # TODO: rysuj swiat

        # zerowanie pola kierunek, czyli ostatniego klikniętego klawisza
        self.__kierunek = Akcje.stoj

        # na koniec dolicz kolejną turę
        self.__tura += 1

    def dodaj_komunikat(self, info):
        self.__komunikaty.append(info)

    def dodaj_organizm(self, typ, miejsce):
        # TODO uzupełnić resztę organizmów
        org = None
        if typ is Rodzaj.wilk:
            org = Wilk(self, miejsce)
        elif typ is Rodzaj.owca:
            org = Owca(self, miejsce)
        elif typ is Rodzaj.zolw:
            org = Zolw(self, miejsce)
        elif typ is Rodzaj.lis:
            org = Lis(self, miejsce)
        else:
            pass
        if org is not None:
            self.__noweOrganizmy.append(org)

    def wczytaj_organizm(self, typ, miejsce, sila, wiek, licznik=None):
        # TODO uzupełnić resztę organizmów
        org = None
        if typ is Rodzaj.wilk:
            org = Wilk(self, miejsce, sila, wiek)
        elif typ is Rodzaj.owca:
            org = Owca(self, miejsce, sila, wiek)
        elif typ is Rodzaj.zolw:
            org = Zolw(self, miejsce, sila, wiek)
        elif typ is Rodzaj.lis:
            org = Lis(self, miejsce, sila, wiek)
        else:
            pass
        if org is not None:
            self.__organizmy.append(org)

    def dodaj_wlasny_organizm(self, typ, miejsce):
        org = {
            "wilk": Wilk(self, miejsce),
            "owca": Owca(self, miejsce),
            "zolw": Zolw(self, miejsce),
            "lis": Lis(self, miejsce)
            # TODO reszta
        }.get(typ, Owca(self, miejsce))
        self.__organizmy.append(org)

    def usun_organizmy(self):
        self.__organizmy = filter(lambda org: org.get_czy_zyje(), self.__organizmy)

    def rysuj_swiat(self):
        """TODO"""

    def zapisz_swiat(self, plik):
        """TODO"""

    def wczytaj_swiat(self, plik):
        """TODO"""

    """roboczo"""
    def __repr__(self):
        return str(self.__kierunek.value)



