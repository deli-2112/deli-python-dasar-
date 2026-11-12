# Bab #16: Penanganan Pengecualian (Try - Except - Else - Finally)

def bagi_bilangan(angka1, angka2):
    try:
        hasil = angka1 / angka2
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi angka dengan nol!")
    except TypeError:
        print("Error: Pastikan kedua input berupa angka!")
    else:
        print(f"Hasil pembagian {angka1} / {angka2} = {hasil}")
    finally:
        print("Proses pengecekan selesai.\n")

# Uji 1: Pembagian normal
bagi_bilangan(20, 4)

# Uji 2: Pembagian dengan nol (memicu ZeroDivisionError)
bagi_bilangan(10, 0)

# Uji 3: Tipe data salah (memicu TypeError)
bagi_bilangan(10, "lima")   