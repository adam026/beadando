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

