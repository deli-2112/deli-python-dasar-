# Bab #9: Daftar (List), Tuple, dan Himpunan (Set)

# 1. List (Daftar) -> Berurutan, bisa diubah (mutable), pakai kurung siku []
bahasa = ["Python", "C++", "HTML"]
bahasa.append("JavaScript")  # Menambah item baru
bahasa[1] = "Java"           # Mengubah item indeks ke-1
print("Isi List:", bahasa)
print("Item pertama List:", bahasa[0])

# 2. Tuple -> Berurutan, TIDAK bisa diubah (immutable), pakai kurung biasa ()
koordinat = (-6.5407, 107.4462)
hari = ("Senin", "Selasa", "Rabu")
print("\nIsi Tuple Koordinat:", koordinat)
print("Hari kedua:", hari[1])

# 3. Set (Himpunan) -> Tidak berurutan, otomatis menghapus duplikat, pakai kurung kurawal {}
angka_unik = {1, 2, 3, 3, 4, 4, 5}
angka_unik.add(6)
print("\nIsi Set (duplikat otomatis hilang):", angka_unik)

# Operasi Himpunan
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Irisan (intersection):", set_a & set_b)
print("Gabungan (union):", set_a | set_b)