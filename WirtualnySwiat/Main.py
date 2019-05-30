from WirtualnySwiat.Swiat import Swiat
from WirtualnySwiat.Wspolrzedne import Wspolrzedne
from WirtualnySwiat.zwierzeta.Owca import Owca

swiat = Swiat(20, 20)
miejsce = Wspolrzedne(1, 2)
owca = Owca(swiat, miejsce, 5, 2)
owca.rysowanie()
print(owca.get_wiek())
