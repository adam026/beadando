from Szobak.Szoba import Szoba


class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, meret, nev, privatPF, kad):
        super().__init__(ar, szobaszam)
        self.meret = meret
        self.nev = nev
        self.privatPF = privatPF
        self.kad = kad