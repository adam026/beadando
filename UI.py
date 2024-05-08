from Foglalasok.FoglalasKezelo import FoglalasKezelo


class UI:
    @staticmethod
    def listaz_szallodak(szallodak):
        print("Elérhető szállodák és szobák:")
        for szalloda in szallodak:
            print(f"- {szalloda.nev}:")
            for szoba in szalloda.szobak:
                print(f"  * Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar} Ft")
    @staticmethod
    def foglalas_menu(foglalaskezelo):
        print("Foglalás menü:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("0. Kilépés")

        while True:
            valasztas = input("Válassz egy menüpontot: ")
            if valasztas == "1":
                szoba_szam = input("Add meg a foglalni kívánt szoba számát: ")
                kezdet = input("Add meg a foglalás kezdeti dátumát (éééé-hh-nn): ")
                veg = input("Add meg a foglalás befejező dátumát (éééé-hh-nn): ")
                FoglalasKezelo.foglalas(szoba_szam, kezdet, veg)
            elif valasztas == "2":
                szoba_szam = input("Add meg a lemondani kívánt foglalás szoba számát: ")
                kezdet = input("Add meg a foglalás kezdeti dátumát (éééé-hh-nn): ")
                veg = input("Add meg a foglalás befejező dátumát (éééé-hh-nn): ")
                FoglalasKezelo.lemondas(szoba_szam, kezdet, veg)
            elif valasztas == "3":
                FoglalasKezelo.listaz()
            elif valasztas == "0":
                print("Kilépés...")
                break
            else:
                print("Érvénytelen választás!")