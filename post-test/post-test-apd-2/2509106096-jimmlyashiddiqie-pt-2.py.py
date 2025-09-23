DISKON_ACER = 5
DISKON_ASUS = 7
DISKON_LENOVO = 10

def format_rupiah(angka):
    integer_part = int(angka)
    desimal_part = f"{angka % 1:.2f}"[2:]
    integer_str = f"{integer_part:,}".replace(',', '.')
    return f"Rp {integer_str},{desimal_part}"

print("=" * 50)
print("                 💻 HITUNG DISKON 💻")
print("=" * 50)

nama = input("MASUKKAN NAMA LENGKAP: ").strip().title()
nim = input("MASUKKAN NIM         : ").strip()

while True:
    try:
        harga = float(input("Masukkan Harga laptop (contoh: 10000000): "))
        if harga > 0:
            break
        else:
            print("Harga harus lebih dari nol, ya! Coba lagi.")
    except ValueError:
        print("⚠️  Input harus berupa angka. Coba lagi!")

harga_acer = harga - (harga * DISKON_ACER / 100)
harga_asus = harga - (harga * DISKON_ASUS / 100)
harga_lenovo = harga - (harga * DISKON_LENOVO / 100)

print("\n" * 2)
print("=" * 50)
print("                    HASILNYA")
print("=" * 50)
print(f"Nama      : {nama}")
print(f"NIM       : {nim}")
print(f"Harga Awal: {format_rupiah(harga)}")
print("-" * 50)

print(f"{'Merek':<12}  |{'Diskon':<8}    |{'Harga Setelah Diskon':<25}")
print("-" * 50)
print(f"{'Acer':<12}  |{DISKON_ACER}%{'':<5}     |{format_rupiah(harga_acer):<25}")
print(f"{'Asus':<12}  |{DISKON_ASUS}%{'':<5}     |{format_rupiah(harga_asus):<25}")
print(f"{'Lenovo':<12}  |{DISKON_LENOVO}%{'':<5}    |{format_rupiah(harga_lenovo):<25}")
print("=" * 50)
print("                Terima kasih! 🔥😎🔥")
print("=" * 50)
