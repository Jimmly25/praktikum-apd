
username_saya = "jimmly ashiddiqie"
password_saya = "2509106096"


for i in range(3):
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username == username_saya and password == password_saya:
        print("Login berhasil!\n")
        break  
    else:
        if i <2:
            print("username dan password salah.")

else:
    print("login gagal")
    exit()
            
while True:
    print("Toko furnitur infordeh")
    print("1. Sofa per unit             = Rp500.000")
    print("2. Meja Belajar per unit     = Rp250.000")
    print("3. Rak Lemari per unit       = Rp150.000")
    print("4. Keluar")

    pilihan = input("Pilih jenis tiket (1-4): ")

    if pilihan not in ["1", "2", "3", "4"]:
        print("Pilihan tidak valid! Silakan masukkan angka 1-4.")
        continue
    if pilihan == "4":
        print("Terima kasih")
        break

    elif pilihan == "1":
        jenis = "Sofa"
        harga = 500000
    elif pilihan == "2":
        jenis = "Meja belajar"
        harga = 250000
    elif pilihan == "3":
        jenis = "Rak lemari"
        harga = 150000
 
    jumlah_input = input("Masukkan jumlah furnitur yang ingin di beli: ")

    if all(char in "0123456789" for char in jumlah_input):
        jumlah = int(jumlah_input)
    else:
        print("Jumlah harus berupa angka!")
        continue

    total = 0
    for i in range(jumlah):
        total += harga  

    potongan = 0 
    bonus = ""

    if total >= 700000:
        potongan = total * 0.20
    elif total >= 500000:
        potongan = total * 0.08
    elif total >= 150000:
        bonus = "kitchen set"

    total_bayar = total - potongan

    print("\n=== STRUK PEMBELIAN ===")
    print(f"Jenis furnituer  : {jenis}")
    print(f"Jumlah furnituer : {jumlah}")
    if total >= 200000:
        print(f"Total harga      : Rp {total:,.0f}")
    if potongan > 0:
         print(f"Potongan ({int((potongan/total)*100)}%)   : Rp {potongan:,.0f}")

    if bonus != "":
        print(f"Bonus          : {bonus}")
    print(f"Total Bayar      : Rp {total_bayar:,.0f}")
    print("===============================\n")

    lanjut = input("Apakah ingin membeli furnituer lagi? (y/n): ").lower()
    if lanjut != 'y':
        print("Terima kasih telah membeli")
        break
