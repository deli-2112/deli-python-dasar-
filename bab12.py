# Bab #12: Enkapsulasi (Pembungkusan & Hak Akses Data)

class TabunganSiswa:
    def __init__(self, nama_pemilik, saldo_awal):
        self.nama_pemilik = nama_pemilik    # Public (bebas diakses)
        self._sekolah = "SMK Negeri"        # Protected (diawali satu garis bawah _)
        self.__saldo = saldo_awal           # Private (diawali dua garis bawah __)

    # Getter untuk membaca atribut private __saldo secara aman
    def cek_saldo(self):
        return self.__saldo

    # Setter/Method untuk mengubah atribut private dengan validasi
    def setor_tunai(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor Rp{jumlah} berhasil.")
        else:
            print("Jumlah setoran harus lebih dari 0.")

tabungan = TabunganSiswa("Deli", 50000)
print("Pemilik:", tabungan.nama_pemilik)
print("Saldo Awal:", tabungan.cek_saldo())

tabungan.setor_tunai(25000)
print("Saldo Terbaru:", tabungan.cek_saldo())