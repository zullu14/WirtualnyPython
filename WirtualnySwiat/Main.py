from random import randint

from WirtualnySwiat.Rodzaj import Rodzaj
from WirtualnySwiat.Swiat import Swiat
from WirtualnySwiat.Wspolrzedne import Wspolrzedne
from WirtualnySwiat.zwierzeta.Owca import Owca
from WirtualnySwiat.zwierzeta.Wilk import Wilk
from WirtualnySwiat.zwierzeta.Zolw import Zolw

if __name__ == "__main__":
    swiat = Swiat(10, 10)
    while True:
        input()
        swiat.wykonaj_ture()