from Szobak.EgyagyasSzoba import EgyagyasSzoba
from Szobak.KetagyasSzoba import KetagyasSzoba


class Adatkezelo:
    def feltolt(szalloda):
        if szalloda.nev == "Wizzarding World Hotel":
            szalloda.add_szoba(EgyagyasSzoba(10000, 101,45,"Lumos", "Wizzard Standard", "Dél-Kelet"))
            szalloda.add_szoba(EgyagyasSzoba(12000, 102, 50, "Depulso", "Wizzard Superior", "Dél-Nyugat"))
            szalloda.add_Szoba(KetagyasSzoba(15000, 103, 60, "Incendio", "Wizzard Delux", "Észak-Kelet"))
            szalloda.add_Szoba(KetagyasSzoba(17000, 104, 70, "Imperio", "Wizzard Apartman", "Észak-Nyugat"))
        elif szalloda.nev == "Middle-Earth Inn":
            szalloda.add_szoba(EgyagyasSzoba(10000, 201, 45, "Moria", "Middle-Earth Standard", "Dél-Kelet"))
            szalloda.add_szoba(EgyagyasSzoba(13000, 202, 50, "Númenor", "Middle-Earth Superior", "Dél-Nyugat"))
            szalloda.add_Szoba(KetagyasSzoba(15000, 203, 60, "Khazad-Dûm", "Middle-Earth Delux", "Észak-Kelet"))
            szalloda.add_Szoba(KetagyasSzoba(18000, 204, 70, "Eregion", "Middle-Earth Apartman", "Észak-Nyugat"))
