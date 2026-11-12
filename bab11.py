# Bab #11: Kelas & Objek (Dasar-dasar OOP)

class Siswa:
    # Konstruktor (__init__) otomatis berjalan saat objek dibuat
    def __init__(self, nama, kelas, jurusan):
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan

    # Method (fungsi di dalam class)
    def perkenalan(self):
        print(f"Halo, saya {self.nama} dari kelas {self.kelas} jurusan {self.jurusan}.")

# Membuat objek (instansiasi) dari class Siswa
siswa1 = Siswa("Deli", "11 SMK", "RPL")
siswa2 = Siswa("Marsya", "11 SMK", "RPL")

# Memanggil atribut dan method dari objek
print("Nama Objek 1:", siswa1.nama)
siswa1.perkenalan()
siswa2.perkenalan()
