from Szobak.Szoba import Szoba


class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, meret, nev, tipus, elhelyezkedes):
        super().__init__(ar, szobaszam)
        self.meret = meret
        self.nev = nev
        self.tipus = tipus
        self.elhelyezkedes = elhelyezkedes
        self.foglalt = []

    def szoba_tipus(self):
        return "Egyágyas szoba"

    def adatok(self):
        print(f"A szoba neve: {self.nev} | Szobaszám: {self.szobaszam} | Ár: {self.ar} | Méret: {self.meret} | Típus: {self.tipus} | Elhelyezkedés: {self.elhelyezkedes}")

