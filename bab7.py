# Bab #7: Alur Kontrol (Percabangan & Perulangan)

# 1. Percabangan (if - elif - else)
print("=== Percabangan Nilai ===")
nilai = 84
if nilai >= 90:
    predikat = "A (Sangat Baik)"
elif nilai >= 80:
    predikat = "B (Baik)"
elif nilai >= 75:
    predikat = "C (Cukup)"
else:
    predikat = "D (Perlu Perbaikan)"
print("Nilai:", nilai, "| Predikat:", predikat)

# 2. Perulangan for dengan range()
print("\n=== Perulangan for ===")
for i in range(1, 6):
    print("Perulangan ke-", i)

# 3. Perulangan while dengan break dan continue
print("\n=== Perulangan while (break & continue) ===")
angka = 0
while angka < 10:
    angka += 1
    if angka == 3:
        continue  # Lewati angka 3, lanjut ke putaran berikutnya
    if angka == 7:
        break     # Hentikan paksa perulangan saat mencapai angka 7
    print("Angka:", angka)