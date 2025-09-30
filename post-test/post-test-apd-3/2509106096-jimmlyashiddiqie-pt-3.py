nama_saya = "jimmly ashiddiqie"
nim_saya = "2509106096"

ukt = 6000000

nama = input("masukkan nama:")
nim = input("masukkan nim:")

if nama == nama_saya and nim == nim_saya:
    print("login berhasil")

    print("pilih metode pembayaran")
    print("1. lunas (admin 1%)")
    print("2. cicilan 2x (adminn 5%)")
    print("3. cicilan 4x (admin 8%)")
    print("4. cicilan 6x (admin 12%)")

    pilihan = input("masukkan pilihan (1, 2, 3, 4,) :")

    if pilihan == "1":
        admin = 0.01
        cicilan = 1
    elif pilihan == "2":
        admin = 0.05
        cicilan = 2
    elif pilihan == "3":
        admin = 0.08
        cicilan = 4
    elif pilihan == "4":
        admin = 0.12
        cicilan = 6
    else: 
         print("pilih 1 sampai 4 saja.")

    total = ukt + (ukt*admin)
    print("total bayar        : Rp {:,}".format(int(total)))
     
    if cicilan > 1:
        print("jumlah cicilan     :",(cicilan),"kali cicilan")
        print("besar per cicilan  : Rp {:,}".format(int(total / cicilan)))

    else: 
        print("pembayaran lunas")


else: 
    print("login gagal nama dan nim salah")

