# Bab #5: Konstantina (Konstanta) dalam Python
from typing import Final

# Penulisan konstanta di Python menggunakan HURUF KAPITAL semua (UPPER_CASE)
PI: Final[float] = 3.14159
GRAVITASI: Final[float] = 9.8
NAMA_SEKOLAH: Final[str] = "SMK Negeri"
MAKSIMAL_SISWA: Final[int] = 36

# Menghitung luas lingkaran menggunakan konstanta PI
jari_jari = 7
luas_lingkaran = PI * (jari_jari ** 2)

print("Nama Sekolah:", NAMA_SEKOLAH)
print("Maksimal Siswa per Kelas:", MAKSIMAL_SISWA)
print("Nilai Gravitasi:", GRAVITASI, "m/s^2")
print("Luas Lingkaran (r=7):", luas_lingkaran)