# Bab #17: Penanganan File (Membaca & Menulis File)

nama_file = "catatan_bab17.txt"

# 1. Menulis file baru (mode 'w' = write)
with open(nama_file, "w", encoding="utf-8") as file:
    file.write("Catatan Praktikum Python Dasar - Bab 17\n")
    file.write("Nama: Novita keren deli | Kelas: 11 SMK jurusan RPL\n")

# 2. Menambahkan baris baru ke file yang sudah ada (mode 'a' = append)
with open(nama_file, "a", encoding="utf-8") as file:
    file.write("Status: Berhasil menulis dan menambah isi file.\n")

# 3. Membaca seluruh isi file (mode 'r' = read)
print("=== Isi File catatan_bab17.txt ===")
with open(nama_file, "r", encoding="utf-8") as file:
    isi = file.read()
    print(isi) 