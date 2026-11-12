# Bab #6: Operator dalam Python

a = 15
b = 4

# 1. Operator Aritmatika
print("=== Operator Aritmatika ===")
print("Penjumlahan (15 + 4):", a + b)
print("Pengurangan (15 - 4):", a - b)
print("Perkalian (15 * 4):", a * b)
print("Pembagian Desimal (15 / 4):", a / b)
print("Pembagian Bulat (15 // 4):", a // b)
print("Sisa Bagi / Modulus (15 % 4):", a % b)
print("Pangkat (15 ** 2):", a ** 2)

# 2. Operator Penugasan (Assignment)
print("\n=== Operator Penugasan ===")
nilai = 10
nilai += 5  # Sama dengan: nilai = nilai + 5
print("Setelah += 5:", nilai)
nilai *= 2  # Sama dengan: nilai = nilai * 2
print("Setelah *= 2:", nilai)

# 3. Operator Perbandingan (Menghasilkan True atau False)
print("\n=== Operator Perbandingan ===")
print("Apakah a == b?", a == b)
print("Apakah a != b?", a != b)
print("Apakah a > b?", a > b)

# 4. Operator Logika (and, or, not)
print("\n=== Operator Logika ===")
lulus_teori = True
lulus_praktik = False
print("Lulus keduanya (and):", lulus_teori and lulus_praktik)
print("Lulus salah satu (or):", lulus_teori or lulus_praktik)
print("Kebalikan lulus_praktik (not):", not lulus_praktik)