from Szalloda.Szalloda import Szalloda
from Szalloda.SzallodaInterface import SzallodaInterface
from Szobak.EgyagyasSzoba import EgyagyasSzoba
from Szobak.KetagyasSzoba import KetagyasSzoba


class Adatkezelo():
    def __init__(self):
        self.szallodak = []

    def kezdo_adatok_feltoltese(self):
        szalloda1 = Szalloda("Wizzarding World Hotel", 5, "Igen")
        szalloda2 = Szalloda("Middle-Earth Inn", 4, "Igen")
        self.szallodak.append(szalloda1)
        self.szallodak.append(szalloda2)

        szalloda1.szoba_hozzaadasa(EgyagyasSzoba(10000, 101, 45, "Lumos", "Wizzard Standard", "Dél-Kelet"))
        szalloda1.szoba_hozzaadasa(EgyagyasSzoba(12000, 102, 50, "Depulso", "Wizzard Superior", "Dél-Nyugat"))
        szalloda1.szoba_hozzaadasa(KetagyasSzoba(15000, 103, 60, "Incendio", "Nem", "Igen"))
        szalloda1.szoba_hozzaadasa(KetagyasSzoba(17000, 104, 70, "Imperio", "Igen", "Igen"))

        szalloda2.szoba_hozzaadasa(EgyagyasSzoba(10000, 201, 45, "Moria", "Middle-Earth Standard", "Dél-Kelet"))
        szalloda2.szoba_hozzaadasa(EgyagyasSzoba(13000, 202, 50, "Númenor", "Middle-Earth Superior", "Dél-Nyugat"))
        szalloda2.szoba_hozzaadasa(KetagyasSzoba(15000, 203, 60, "Khazad-Dûm", "Nem", "Igen"))
        szalloda2.szoba_hozzaadasa(KetagyasSzoba(18000, 204, 70, "Eregion", "Igen", "Igen"))

        szalloda1.szoba_foglalasa(101, "2024-05-08", "2024-05-10")
        szalloda1.szoba_foglalasa(102, "2024-06-15", "2024-06-20")
        szalloda2.szoba_foglalasa(201, "2024-07-01", "2024-07-05")
        szalloda2.szoba_foglalasa(202, "2024-08-10", "2024-08-15")
        szalloda2.szoba_foglalasa(203, "2024-09-01", "2024-09-03")

    def futtat(self):
        while True:
            print("\nVálasszon szállodát:")
            for i, szalloda in enumerate(self.szallodak, start=1):
                print(f"{i}. Szálloda neve: {szalloda.szalloda_neve} | Csillagok száma: {szalloda.csillagok_szama} | Wellness: {szalloda.wellness_reszleg}")

            szalloda_valasztas = input("Kérem adja meg a választott szálloda sorszámát: ")
            if not szalloda_valasztas.isdigit() or int(szalloda_valasztas) < 1 or int(szalloda_valasztas) > len(self.szallodak):
                print("Nem érvényes szálloda sorszám.")
                continue

            szalloda_index = int(szalloda_valasztas) - 1
            akt_szalloda = self.szallodak[szalloda_index]
            akt_szalloda_interface = SzallodaInterface(akt_szalloda)
            akt_szalloda_interface.futtat()

