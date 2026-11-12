# Bab #10: Kamus (Dictionary) dalam Python

# Membuat dictionary dengan pasangan key: value
siswa = {
    "nama": "Deli",
    "kelas": "10 SMK",
    "jurusan": "RPL",
    "nilai_rata": 90.5
}

# 1. Mengakses data berdasarkan key
print("Nama Siswa:", siswa["nama"])
print("Jurusan (pakai .get):", siswa.get("jurusan"))
print("Alamat (key belum ada):", siswa.get("alamat", "Belum diisi"))

# 2. Menambah dan mengubah data
siswa["sekolah"] = "SMK Negeri"  # Menambah pasangan key-value baru
siswa["nilai_rata"] = 92.0       # Mengubah nilai pada key yang sudah ada

# 3. Menghapus data
del siswa["kelas"]

# 4. Menampilkan seluruh pasangan key dan value dengan perulangan
print("\n=== Data Lengkap Kamus Siswa ===")
for kunci, nilai in siswa.items():
    print(f"{kunci} : {nilai}")