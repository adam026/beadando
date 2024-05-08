from datetime import datetime
from Foglalasok.Foglalas import Foglalas


class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szoba_szam, kezdet, veg):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szoba_szam:
                foglalas_kezdet = datetime.strptime(kezdet, '%Y-%m-%d')
                foglalas_veg = datetime.strptime(veg, '%Y-%m-%d')
                if foglalas_kezdet > foglalas_veg:
                    print("A foglalás kezdő dátuma nem lehet később, mint a befejező dátum!")
                    return
                if foglalas_kezdet < datetime.now():
                    print("A foglalás csak jövőbeli dátumra lehetséges!")
                    return
                for foglalas in self.foglalasok:
                    if foglalas.szoba == szoba:
                        if(foglalas_kezdet >= foglalas.kezdet and foglalas_kezdet < foglalas.veg) or \
                           (foglalas_veg > foglalas.kezdet and foglalas_veg <= foglalas.veg) or \
                           (foglalas_kezdet <= foglalas.kezdet and foglalas_veg >= foglalas.veg):
                            print("A szoba ezen az időszakban már foglalt!")
                            return
                self.foglalasok.append(Foglalas(szoba, foglalas_kezdet, foglalas_veg))
                print("A foglalás sikeresen rögzítve.")
                return
        print("A megadott szobaszám nem létezik a szállodában.")

    def lemondas(self, szoba_szam, kezdet, veg):
        foglalas_kezdet = datetime.strptime(kezdet, '%Y-%m-%d')
        foglalas_veg = datetime.strptime(veg, '%Y-%m-%d')
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szoba_szam and foglalas.kezdet == foglalas_kezdet and foglalas.veg == foglalas_veg:
                self.foglalasok.remove(foglalas)
                print("A foglalás sikeresen törölve.")
                return
        print("Nem található foglalás a megadott szobaszámmal és időszakkal.")

    def listaz(self):
        print("Összes foglalás:")
        for foglalas in self.foglalasok:
            print(
                f"  Szoba: {foglalas.szoba.szobaszam}, Kezdet: {foglalas.kezdet.strftime('%Y-%m-%d')}, Vég: {foglalas.veg.strftime('%Y-%m-%d')}")