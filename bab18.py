# Bab #18: Modul (Mengimpor Modul Bawaan & Modul Buatan Sendiri)
import math
import modul_matematika

# Menggunakan modul bawaan Python (math)
print("Akar kuadrat dari 64:", math.sqrt(64))
print("Nilai Pi dari modul math:", math.pi)

# Menggunakan modul buatan sendiri (modul_matematika.py)
hasil_tambah = modul_matematika.tambah(15, 10)
hasil_kali = modul_matematika.kali(6, 7)

print("Hasil tambah (15 + 10):", hasil_tambah)
print("Hasil kali (6 * 7):", hasil_kali) 