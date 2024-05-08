class SzallodaInterfesz:
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
        szobaszam = self.szobaszam_bekero()
        kezdo_datum = input("Kérem adja meg a foglalás kezdeti dátumát (YYYY-MM-DD formátumban): ")
        vegso_datum = input("Kérem adja meg a foglalás végdátumát (YYYY-MM-DD formátumban): ")

        foglalas = self.szalloda.szoba_foglalasa(szobaszam, kezdo_datum, vegso_datum)
        if foglalas:
            print(f"A foglalás ára: {self.szalloda.foglalas_ar_szamitas(foglalas)}")

    def foglalas_lemondasa(self):
        szobaszam = self.szobaszam_bekero()
        kezdo_datum = input("Kérem adja meg a lemondani kívánt foglalás kezdeti dátumát (YYYY-MM-DD formátumban): ")
        vegso_datum = input("Kérem adja meg a lemondani kívánt foglalás végdátumát (YYYY-MM-DD formátumban): ")

        for szoba in self.szalloda.szobak:
            for foglalas in szoba.foglalt:
                if (foglalas.szoba.szobaszam == szobaszam) and (
                        foglalas.kezdo_datum.strftime("%Y-%m-%d") == kezdo_datum) and (
                        foglalas.vegso_datum.strftime("%Y-%m-%d") == vegso_datum):
                    self.szalloda.foglalas_lemondasa(foglalas)
                    return

        print("Nem található ilyen foglalás.")

    def foglalasok_listazasa(self):
        self.szalloda.foglalasok_listazasa()

    def szobaszam_bekero(self):
        while True:
            szobaszam = int(input("Kérem adja meg a foglalni kívánt szoba számát: "))
            if szobaszam not in self.szalloda.szoba_szamok():
                print("A megadott szobaszám nem megfelelő!")
                continue
            else:
                break
        return szobaszam
