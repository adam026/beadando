from Szobak.EgyagyasSzoba import EgyagyasSzoba
from Szobak.KetagyasSzoba import KetagyasSzoba


class Szalloda(EgyagyasSzoba, KetagyasSzoba):
    def __init__(self, szallodaNeve, ar, szobaszam, meret, nev, tipus, elhelyezkedes, privatPF, kad):
        EgyagyasSzoba.__init__(ar, szobaszam, meret, nev, tipus, elhelyezkedes)
        KetagyasSzoba.__init__(ar, szobaszam, meret, nev, privatPF, kad)
        self.szallodaNeve = szallodaNeve