# Bab #14: Polimorfisme (Banyak Bentuk)

class Kucing:
    def bersuara(self):
        return "Meong!"

class Anjing:
    def bersuara(self):
        return "Guk guk!"

class Burung:
    def bersuara(self):
        return "Cuit cuit!"

# Satu antarmuka method yang sama menghasilkan perilaku berbeda
daftar_hewan = [Kucing(), Anjing(), Burung()]

for hewan in daftar_hewan:
    print(f"{hewan.__class__.__name__} bersuara: {hewan.bersuara()}")