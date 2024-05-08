class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda

    def foglalas(self, szalloda_index, szoba_index, kezdet, veg):
        szoba = self.szalloda[szalloda_index].szobak[szoba_index]
        if szoba.foglal(kezdet, veg):
            print("A foglalás sikeresen rögzítve.")
        else:
            print("A megadott időszakban a szoba már foglalt!")

    def lemondas(self, szalloda_index, szoba_index, kezdet, veg):
        szoba = self.szalloda[szalloda_index].szobak[szoba_index]
        szoba.lemond(kezdet, veg)
        print("A foglalás sikeresen törölve.")

    def foglalasok_listazasa(self, szalloda_index, szoba_index):
        szoba = self.szalloda[szalloda_index].szobak[szoba_index]
        szoba.foglalasok_listazasa()