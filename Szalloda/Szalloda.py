class Szalloda():
    def __init__(self, szallodaNeve, csillagokSzama, wellnessReszleg):
        self.szallodaNeve = szallodaNeve
        self.csillagokSzama = csillagokSzama
        self.wellnessReszleg = wellnessReszleg
        self.szobak = []

    def add_Szoba(self, szoba):
        self.szobak.append(szoba)
