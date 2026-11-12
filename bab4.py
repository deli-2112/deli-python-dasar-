# Bab #4: Variabel dalam Python

# 1. Membuat dan Mengisi Variabel (Menggunakan gaya penulisan snake_case)
nama_lengkap = "Deli"
umur = 16
nilai_ujian = 92.5

print("Nama:", nama_lengkap)
print("Umur:", umur)
print("Nilai Ujian:", nilai_ujian)

# 2. Mengubah Nilai Variabel (Re-assignment)
# Nilai maupun tipe data di dalam variabel bisa langsung ditimpa
umur = 17
nilai_ujian = "Lulus Sempurna"
print("Umur setelah ulang tahun:", umur)
print("Status Nilai sekarang:", nilai_ujian)

# 3. Multiple Assignment (Mengisi beberapa variabel dalam satu baris)
kelas, jurusan, aktif = "X", "RPL", True
print("Kelas:", kelas, "| Jurusan:", jurusan, "| Aktif:", aktif)

# Memberikan satu nilai yang sama ke beberapa variabel sekaligus
x = y = z = 100
print("Nilai x, y, z:", x, y, z)

# 4. Menghapus Variabel dengan Perintah del
data_sementara = "Data ini akan dihapus"
print("Sebelum dihapus:", data_sementara)
del data_sementara
# Jika print(data_sementara) dijalankan setelah baris ini, Python akan memunculkan NameError