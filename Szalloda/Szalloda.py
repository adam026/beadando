from Foglalasok.Foglalas import Foglalas


class Szalloda:
    def __init__(self, szalloda_neve, csillagok_szama, wellness_reszleg):
        self.szalloda_neve = szalloda_neve
        self.csillagok_szama = csillagok_szama
        self.wellness_reszleg = wellness_reszleg
        self.szobak = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def szobak_listazasa(self):
        for szoba in self.szobak:
            if szoba.szoba_tipus() == "Egyágyas szoba":
                szoba.adatok()
            elif szoba.szoba_tipus() == "Kétágyas szoba":
                szoba.adatok()

    def szoba_foglalasa(self, szobaszam, kezdo_datum, vegso_datum):
        for szoba in self.szobak:
            if szoba.szobaszam == int(szobaszam):
                foglalas = Foglalas(szoba, kezdo_datum, vegso_datum)
                if foglalas.foglalas_ellenorzese(szoba):
                    print("Foglalás sikeres!")
                    return foglalas
                else:
                    print("A szoba már foglalt az adott időszakra.")
                    return None
        print("Nincs ilyen szobaszám a szállodában.")
        return None

    def foglalasok_listazasa(self):
        for szoba in self.szobak:
            for foglalas in szoba.foglalt:
                foglalas.foglalas_megjelenitese()

    def szoba_szamok(self):
        szoba_szamok = []
        for szoba in self.szobak:
            szoba_szamok.append(szoba.szobaszam)
        return szoba_szamok
