from Szobak import Szoba
import datetime

foglalasok = {
    "Szoba" : Szoba,
    "Datum" : datetime.datetime.now(),
    "Ar" : Szoba.ar()
}

class Foglalas():

    def __init__(self, szoba, kezdet, veg):
        self.szoba = szoba
        self.kezdet = kezdet
        self.veg = veg

    def Elerheto(self, Szoba, Kezdodatum):
        if(foglalasok.__contains__(Szoba) &)

    def Lefoglal(self, Szoba, Datum):
