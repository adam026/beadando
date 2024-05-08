from datetime import datetime


class Foglalas:
    def __init__(self, szoba, kezdo_datum, vegso_datum):
        self.szoba = szoba
        self.kezdo_datum = datetime.strptime(kezdo_datum, "%Y-%m-%d")
        self.vegso_datum = datetime.strptime(vegso_datum, "%Y-%m-%d")

    def foglalas_megjelenitese(self):
        print(
            f"Kezdet: {self.kezdo_datum}, Vége: {self.vegso_datum}, Szobaszám: {self.szoba.szobaszam}, Ár: {self.foglalas_ar_szamitas()}")

    def foglalas_lemondasa(self):
        self.szoba.foglalt.remove(self)
        print("Foglalás sikeresen törölve.")

    def foglalas_ellenorzese(self, szoba):
        for foglalas in szoba.foglalt:
            if (self.kezdo_datum <= foglalas.vegso_datum) and (
                    self.vegso_datum >= foglalas.kezdo_datum):
                return False
        szoba.foglalt.append(self)
        return True

    def foglalas_ar_szamitas(self):
        napok_szama = (self.vegso_datum - self.kezdo_datum).days
        return napok_szama * self.szoba.ar
