from random import randint

from WirtualnySwiat.Akcje import Akcje
from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Roslina import Roslina
from WirtualnySwiat.Wspolrzedne import Wspolrzedne
from WirtualnySwiat.Zwierze import Zwierze
from WirtualnySwiat.grafika.OknoSwiat import OknoSwiat
from WirtualnySwiat.rosliny.Guarana import Guarana
from WirtualnySwiat.rosliny.Mlecz import Mlecz
from WirtualnySwiat.rosliny.Sosnowski import Sosnowski
from WirtualnySwiat.rosliny.Trawa import Trawa
from WirtualnySwiat.rosliny.WilczeJagody import WilczeJagody
from WirtualnySwiat.zwierzeta.Antylopa import Antylopa
from WirtualnySwiat.zwierzeta.CyberOwca import CyberOwca
from WirtualnySwiat.zwierzeta.Czlowiek import Czlowiek
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
        self.__okno = OknoSwiat(self)
        self.stworz_swiat()
        self.__okno.show()

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
        populacja = self.__rows * self.__cols / 12
        x = randint(0, self.__rows - 1)
        y = randint(0, self.__cols - 1)
        zajete = False

        # stworz czlowieka i cyber-owce
        self.dodaj_organizm(Rodzaj.czlowiek, Wspolrzedne(x, y))

        while True:
            x = randint(0, self.__rows - 1)
            y = randint(0, self.__cols - 1)
            zajete = False
            for org in self.get_nowe_organizmy():
                if org.get_polozenie().x == x and org.get_polozenie().y == y:
                    zajete = True
                    break
            if not zajete:
                self.dodaj_organizm(Rodzaj.cyberowca, Wspolrzedne(x, y))
                break

        i = 0
        while i < populacja:
            x = randint(0, self.__rows - 1)
            y = randint(0, self.__cols - 1)
            zajete = False
            for org in self.__noweOrganizmy:
                if org.get_polozenie().x == x and org.get_polozenie().y == y:
                    zajete = True
                    break
            if not zajete:
                r = randint(1, len(Rodzaj)-2)
                self.dodaj_organizm(Rodzaj(r), Wspolrzedne(x, y))
                i += 1

        self.dodaj_nowe_organizmy()
        self.rysuj_swiat()
        self.__tura += 1

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
        self.dodaj_nowe_organizmy()

        # narysuj obecny stan świata wraz z komunikatami
        self.rysuj_swiat()

        # zerowanie pola kierunek, czyli ostatniego klikniętego klawisza
        self.__kierunek = Akcje.stoj

        # na koniec dolicz kolejną turę
        self.__tura += 1

    def dodaj_komunikat(self, info):
        self.__komunikaty.append(info)

    def dodaj_organizm(self, typ, miejsce):
        org = None
        if typ is Rodzaj.wilk:
            org = Wilk(self, miejsce)
        elif typ is Rodzaj.owca:
            org = Owca(self, miejsce)
        elif typ is Rodzaj.zolw:
            org = Zolw(self, miejsce)
        elif typ is Rodzaj.lis:
            org = Lis(self, miejsce)
        elif typ is Rodzaj.antylopa:
            org = Antylopa(self, miejsce)
        elif typ is Rodzaj.trawa:
            org = Trawa(self, miejsce)
        elif typ is Rodzaj.mlecz:
            org = Mlecz(self, miejsce)
        elif typ is Rodzaj.guarana:
            org = Guarana(self, miejsce)
        elif typ is Rodzaj.jagody:
            org = WilczeJagody(self, miejsce)
        elif typ is Rodzaj.barszcz:
            org = Sosnowski(self, miejsce)
        elif typ is Rodzaj.czlowiek:
            org = Czlowiek(self, miejsce)
        elif typ is Rodzaj.cyberowca:
            org = CyberOwca(self, miejsce)
        else:
            pass
        if org is not None:
            self.__noweOrganizmy.append(org)

    def wczytaj_organizm(self, typ, miejsce, sila, wiek, licznik=None):
        org = None
        if typ is Rodzaj.wilk:
            org = Wilk(self, miejsce, sila, wiek)
        elif typ is Rodzaj.owca:
            org = Owca(self, miejsce, sila, wiek)
        elif typ is Rodzaj.zolw:
            org = Zolw(self, miejsce, sila, wiek)
        elif typ is Rodzaj.lis:
            org = Lis(self, miejsce, sila, wiek)
        elif typ is Rodzaj.antylopa:
            org = Antylopa(self, miejsce, sila, wiek)
        elif typ is Rodzaj.trawa:
            org = Trawa(self, miejsce, sila, wiek)
        elif typ is Rodzaj.mlecz:
            org = Mlecz(self, miejsce, sila, wiek)
        elif typ is Rodzaj.guarana:
            org = Guarana(self, miejsce, sila, wiek)
        elif typ is Rodzaj.jagody:
            org = WilczeJagody(self, miejsce, sila, wiek)
        elif typ is Rodzaj.barszcz:
            org = Sosnowski(self, miejsce, sila, wiek)
        elif typ is Rodzaj.czlowiek:
            org = Czlowiek(self, miejsce, sila, wiek, licznik)
        elif typ is Rodzaj.cyberowca:
            org = CyberOwca(self, miejsce, sila, wiek)
        else:
            pass
        if org is not None:
            self.__organizmy.append(org)

    def dodaj_wlasny_organizm(self, typ, miejsce):
        org = {
            "wilk": Wilk(self, miejsce),
            "owca": Owca(self, miejsce),
            "zolw": Zolw(self, miejsce),
            "lis": Lis(self, miejsce),
            "antylopa": Antylopa(self, miejsce),
            "trawa": Trawa(self, miejsce),
            "mlecz": Mlecz(self, miejsce),
            "guarana": Guarana(self, miejsce),
            "wilcze jagody": WilczeJagody(self, miejsce),
            "barszcz Sosnowskiego": Sosnowski(self, miejsce),
            "cyber-owca": CyberOwca(self, miejsce)
        }.get(typ, Owca(self, miejsce))
        self.__organizmy.append(org)

    def dodaj_nowe_organizmy(self):
        """Rozmnażanie zwierząt/ rozprzestrzenianie roślin - umieszcza nowy organizm"""
        for nowy_org in self.__noweOrganizmy:
            zajete = False
            for org in self.__organizmy:
                if org.get_polozenie() == nowy_org.get_polozenie():
                    zajete = True
                    break
            if not zajete:
                if isinstance(nowy_org, Zwierze):
                    self.dodaj_komunikat("Nowe zwierze: " + nowy_org.get_typ().name +
                                         " rodzi sie na pozycji " + str(nowy_org.get_polozenie().x) + "," +
                                         str(nowy_org.get_polozenie().y) + ". ")
                elif isinstance(nowy_org, Roslina):
                    self.dodaj_komunikat("Nowa roslina: " + nowy_org.get_typ().name +
                                         " wyrasta na pozycji " + str(nowy_org.get_polozenie().x) + "," +
                                         str(nowy_org.get_polozenie().y) + ". ")
            else:           # jezeli miejsce zajęte, to nie powstanie tu nowy organizm
                nowy_org.set_czy_zyje(False)
        self.__noweOrganizmy = [org1 for org1 in self.__noweOrganizmy if org1.get_czy_zyje()]
        self.__organizmy.extend(self.__noweOrganizmy)
        self.__noweOrganizmy.clear()

    def usun_organizmy(self):
        self.__organizmy = [org for org in self.__organizmy if org.get_czy_zyje()]

    def rysuj_swiat(self):
        self.__okno.rysuj_organizmy()
        if self.__tura > 0:
            self.__okno.ustaw_komunikaty()
        self.__okno.ustaw_panel_sterowania()
        self.__komunikaty.clear()

    def zapisz_swiat(self):
        """zapis do pliku"""
        plik = open("swiat.txt", "w+")
        s = str(self.__rows) + "\n"
        plik.write(s)
        s = str(self.__cols) + "\n"
        plik.write(s)
        s = str(self.__tura) + "\n"
        plik.write(s)
        s = str(len(self.__organizmy)) + "\n"
        plik.write(s)
        for org in self.__organizmy:
            plik.write(org.zapisz_organizm())
            plik.write("\n")
        plik.close()

    def wczytaj_swiat(self):
        """odczyt z pliku"""
        plik = open("swiat.txt", "r")
        wys = int(plik.readline())
        szer = int(plik.readline())
        tura = int(plik.readline())
        n = int(plik.readline())
        if wys > 0 and szer > 0:
            self.__organizmy.clear()
            if self.__rows != wys or self.__cols != szer:
                self.__rows = wys
                self.__cols = szer
                self.__okno.reset_planszy()
            self.__tura = tura

            for i in range(n):
                typ, x, y, sila, wiek, licz = plik.readline().split()
                self.wczytaj_organizm(Rodzaj[typ], Wspolrzedne(int(x), int(y)), int(sila), int(wiek), int(licz))
            self.rysuj_swiat()
            self.__okno.ustaw_panel_sterowania("Wczytany ostatni zapis z pliku. ")
            plik.close()
            return True
        else:
            print("Zle wymiary wczytanego swiata!")
            plik.close()
            return False




