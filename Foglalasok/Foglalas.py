from datetime import datetime


class Foglalas:
    def __init__(self, szoba, kezdo_datum, vegso_datum):
        self.szoba = szoba
        self.kezdo_datum = datetime.strptime(kezdo_datum, "%Y-%m-%d")
        self.vegso_datum = datetime.strptime(vegso_datum, "%Y-%m-%d")

    def foglalas_megjelenitese(self):
        print(
            f"Kezdet: {self.kezdo_datum}, Vége: {self.vegso_datum}, Szobaszám: {self.szoba.szobaszam}, Napi ár: {self.szoba.ar}")