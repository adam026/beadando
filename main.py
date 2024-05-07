from Szobak.EgyagyasSzoba import EgyagyasSzoba
from Szobak.KetagyasSzoba import KetagyasSzoba

EgyagyasSzoba elsoEgyagyas = EgyagyasSzoba(25000, 1, 50, "ElsoEgyagyas", "Superior", "Észak-Nyugat")
EgyagyasSzoba masodikEgyagyas = EgyagyasSzoba(30000, 2, 70, "MasodikEgyagyas", "Business", "Észak-Kelet")
EgyagyasSzoba harmadikEgyagyas = EgyagyasSzoba(20000, 3, 40, "ElsoEgyagyas", "Standard", "Dél-Nyugat")

KetagyasSzoba elsoKetagyas = KetagyasSzoba(35000, 4, 75, "ElsoKetagyas", False, False)
KetagyasSzoba masodikKetagyas = KetagyasSzoba(40000, 5, 85, "MasodikKetagyas", False, True)
KetagyasSzoba harmadikKetagyas = KetagyasSzoba(45000, 6, 90, "HarmadikKetagyas", True, True)

Szalloda elsoSzalloda = Szalloda(elsoEgyagyas, elsoKetagyas)
Szalloda masodikSzalloda = Szalloda(masodikEgyagyas, masodikKetagyas)
Szalloda harmadikSzalloda = Szalloda(harmadikEgyagyas, harmadikKetagyas)
