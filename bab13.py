# Bab #13: Warisan (Inheritance)

# Kelas Induk (Parent Class)
class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info_dasar(self):
        print(f"Kendaraan: {self.merk} (Tahun {self.tahun})")

# Kelas Anak (Child Class) mewarisi sifat dari Kendaraan
class Motor(Kendaraan):
    def __init__(self, merk, tahun, jenis_transmisi):
        super().__init__(merk, tahun)  # Memanggil konstruktor kelas induk
        self.jenis_transmisi = jenis_transmisi

    def info_lengkap(self):
        self.info_dasar()
        print(f"Transmisi: {self.jenis_transmisi}")

motor1 = Motor("Honda Vario", 2024, "Otomatis (Matic)")
motor1.info_lengkap()