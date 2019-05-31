from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Swiat import Swiat
from WirtualnySwiat.Wspolrzedne import Wspolrzedne
from WirtualnySwiat.zwierzeta.Owca import Owca
from WirtualnySwiat.zwierzeta.Wilk import Wilk
from WirtualnySwiat.zwierzeta.Zolw import Zolw

if __name__ == "__main__":
    swiat = Swiat(20, 20)
    miejsce = Wspolrzedne(1, 2)
    wilk = Wilk(swiat, miejsce)
    owca = Owca(swiat, miejsce)
    zolw = Zolw(swiat, miejsce)
    orgs = [wilk, owca, zolw]
    for o in orgs:
        o.rysowanie()
    wilk.kolizja(owca)
    wilk.kolizja(zolw)
    orgs = filter(lambda org: org.get_czy_zyje(), orgs)
    print()
    for o in orgs:
        o.rysowanie()
