# Bab #8: Fungsi (Function) dalam Python

# 1. Fungsi dasar tanpa parameter
def sapa_pengguna():
    print("Halo! Selamat datang di praktikum Python Dasar.")

# 2. Fungsi dengan parameter dan nilai default
def perkenalan(nama, jurusan="Rekayasa Perangkat Lunak"):
    print(f"Nama: {nama} | Jurusan: {jurusan}")

# 3. Fungsi dengan nilai kembalian (return)
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

# 4. Fungsi Lambda (fungsi ringkas satu baris)
hitung_kuadrat = lambda x: x ** 2

# Memanggil semua fungsi
sapa_pengguna()
perkenalan("Deli")
perkenalan("Budi", "Teknik Komputer dan Jaringan")

hasil_luas = hitung_luas_persegi_panjang(12, 5)
print("Luas Persegi Panjang (12x5):", hasil_luas)
print("Kuadrat dari 6 (Lambda):", hitung_kuadrat(6))