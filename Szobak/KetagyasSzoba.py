from Szobak.Szoba import Szoba


class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, meret, nev, privatPF, kad):
        super().__init__(ar, szobaszam)
        self.meret = meret
        self.nev = nev
        self.privatPF = privatPF
        self.kad = kad
        self.foglalt = []

    def szoba_tipus(self):
        return "Kétágyas szoba"

    def adatok(self):
        print(f"A szoba neve: {self.nev} | Szobaszám: {self.szobaszam} | Ár: {self.ar} | Méret: {self.meret} | Privát pezsgőfürdő: {self.privatPF} | Kád: {self.kad}")