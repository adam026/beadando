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
            print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar}, Típus: {szoba.szoba_tipus()}")

    def szoba_foglalasa(self, szobaszam, kezdo_datum, vegso_datum):
        for szoba in self.szobak:
            if szoba.szobaszam == int(szobaszam):
                foglalas = Foglalas(szoba, kezdo_datum, vegso_datum)
                if self.ellenoriz_foglalast(szoba, foglalas):
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

    @staticmethod
    def foglalas_ar_szamitas(foglalas):
        napok_szama = (foglalas.vegso_datum - foglalas.kezdo_datum).days
        return napok_szama * foglalas.szoba.ar

    @staticmethod
    def foglalas_lemondasa(foglalas):
        foglalas.szoba.foglalt.remove(foglalas)
        print("Foglalás sikeresen törölve.")

    @staticmethod
    def ellenoriz_foglalast(szoba, foglalas):
        for foglalt_foglalas in szoba.foglalt:
            if (foglalas.kezdo_datum <= foglalt_foglalas.vegso_datum) and (foglalas.vegso_datum >= foglalt_foglalas.kezdo_datum):
                return False
        szoba.foglalt.append(foglalas)
        return True

    def szoba_szamok(self):
        szoba_szamok = []
        for szoba in self.szobak:
            szoba_szamok.append(szoba.szobaszam)
        return szoba_szamok

