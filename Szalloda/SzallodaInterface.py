from datetime import datetime


class SzallodaInterface:
    def __init__(self, szalloda):
        self.szalloda = szalloda

    def futtat(self):
        while True:
            print("\nVálasszon műveletet:")
            print("1. Szobafoglalás")
            print("2. Foglalás lemondása")
            print("3. Foglalások listázása")
            print("4. Vissza a szállodákhoz")

            valasztas = input("Kérem adja meg a választott művelet sorszámát: ")

            if valasztas == "1":
                self.szobafoglalas_felvetele()
            elif valasztas == "2":
                self.foglalas_lemondasa()
            elif valasztas == "3":
                self.foglalasok_listazasa()
            elif valasztas == "4":
                print("Vissza a szállodákhoz.")
                break
            else:
                print("Nem érvényes választás.")

    def szobafoglalas_felvetele(self):
        self.szalloda.szobak_listazasa()
        szobaszam = self.szobaszam_bekero("foglalni")
        kezdo_datum = self.kezdodatum_bekero("foglalni")
        vegso_datum = self.vegso_datum_bekero("foglalás", kezdo_datum)

        foglalas = self.szalloda.szoba_foglalasa(szobaszam, kezdo_datum, vegso_datum)
        if foglalas:
            print(f"A foglalás ára: {foglalas.foglalas_ar_szamitas()}")

    def foglalas_lemondasa(self):
        szobaszam = self.szobaszam_bekero("lemondani")
        kezdo_datum = self.kezdodatum_bekero("lemondani kívánt foglalás")
        vegso_datum = self.vegso_datum_bekero("lemondani kívánt foglalás", kezdo_datum)

        for szoba in self.szalloda.szobak:
            for foglalas in szoba.foglalt:
                if (foglalas.szoba.szobaszam == szobaszam) and (
                        foglalas.kezdo_datum.strftime("%Y-%m-%d") == kezdo_datum) and (
                        foglalas.vegso_datum.strftime("%Y-%m-%d") == vegso_datum):
                    foglalas.foglalas_lemondasa()
                    return

        print("Nem található ilyen foglalás.")

    def foglalasok_listazasa(self):
        self.szalloda.foglalasok_listazasa()

    def szobaszam_bekero(self, kifejezes):
        while True:
            szobaszam_input = input(f"Kérem adja meg a {kifejezes} kívánt szoba számát: ")
            try:
                szobaszam = int(szobaszam_input)
            except ValueError:
                print("Hibás szobaszám formátum. Kérem adjon meg egy számot!")
                continue

            if szobaszam not in self.szalloda.szoba_szamok():
                print("A megadott szobaszám nem megfelelő!")
                continue

            break
        return int(szobaszam_input)

    @staticmethod
    def kezdodatum_bekero(kifejezes):
        while True:
            kezdo_datum_str = input(f"Kérem adja meg a {kifejezes} kezdeti dátumát (YYYY-MM-DD formátumban): ")

            try:
                kezdo_datum = datetime.strptime(kezdo_datum_str, "%Y-%m-%d")
            except ValueError:
                print("Hibás dátum formátum. Kérem adja meg a dátumot újra!")
                continue

            if kezdo_datum < datetime.now():
                print("A foglalás kezdeti dátuma nem lehet múltbeli. Kérem adjon meg egy jövőbeli dátumot!")
                continue

            break
        return kezdo_datum_str

    @staticmethod
    def vegso_datum_bekero(kifejezes, kezdo_datum):
        while True:
            vegso_datum_str = input(f"Kérem adja meg a {kifejezes} végdátumát (YYYY-MM-DD formátumban): ")

            try:
                vegso_datum = datetime.strptime(vegso_datum_str, "%Y-%m-%d")
            except ValueError:
                print("Hibás dátum formátum. Kérem adja meg a dátumot újra!")
                continue

            if vegso_datum < datetime.now():
                print("Kérem adjon meg egy jövőbeli dátumot!")
                continue

            if vegso_datum <= datetime.strptime(kezdo_datum, "%Y-%m-%d"):
                print("A foglalás végdátuma nem lehet korábban, mint a kezdő dátuma!")
                continue

            break
        return vegso_datum_str
