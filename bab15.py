# Bab #15: Abstraksi (Abstract Base Class)
from abc import ABC, abstractmethod

# Kelas Abstrak (tidak bisa dijadikan objek secara langsung)
class BangunDatar(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

# Kelas Turunan wajib mengimplementasikan method abstrak
class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi * self.sisi

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

persegi = Persegi(6)
segitiga = Segitiga(10, 4)

print("Luas Persegi (sisi 6):", persegi.hitung_luas())
print("Luas Segitiga (alas 10, tinggi 4):", segitiga.hitung_luas())