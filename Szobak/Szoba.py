from abc import ABC


class Szoba(ABC):
    pass


def __init__(self):
    self.ar = 0
    self.szobaszam = 0


@property
def ar(self):
    return self._ar


@property
def szobaszam(self):
    return self._szobaszam


@ar.setter
def ar(self, value):
    if value > 0:
        self._ar = value
    else:
        print("Az ár nem lehet negatív!")


@szobaszam.setter
def szobaszam(self, value):
    if value > 0:
        self._szobaszam = value
    else:
        print("A szobaszám nem lehet negatív")
