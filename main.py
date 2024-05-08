from Adatkezelo import Adatkezelo
from Foglalasok.FoglalasKezelo import FoglalasKezelo
from Szalloda.Szalloda import Szalloda
from UI import UI

wizzarding_world = Szalloda("Wizzarding World Hotel")
middle_earth = Szalloda("Middle-earth Inn")

Adatkezelo.feltolt(wizzarding_world)
Adatkezelo.feltolt(middle_earth)

szallodak = [wizzarding_world, middle_earth]

UI.listaz_szallodak(szallodak)

while True:
    print("Válassza ki a szállodát, ahol szobát szeretne foglalni. Elérhető szállodák: \nA) Wizzarding World Hotel \nB) Middle-Earth Inn")
foglalaskezelo = FoglalasKezelo(wizzarding_world)
InterakcioKezelo.foglalas_menu(foglalaskezelo)