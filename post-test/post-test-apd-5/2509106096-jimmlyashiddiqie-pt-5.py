akun = [["admin", "admin123", "admin"]]
data_pemain = []
program_jalan = True

while program_jalan:
    print("""
==============================
     SISTEM LOGIN ESPORT
==============================
1. Login
2. Register
""")

    menu_awal = input("Pilih menu (1-2): ")

    if menu_awal == "1":
        print("=== LOGIN ===")
        user = input("Username: ")
        pw = input("Password: ")

        role = ""
        for a in akun:
            if a[0] == user and a[1] == pw:
                role = a[2]

        if role == "admin":
            print("\nLogin berhasil sebagai ADMIN\n")

            while True:
                print("""
==============================
    MANAJEMEN TIM ESPORT 
          (ADMIN)
==============================
1. Tambah Pemain
2. Lihat Pemain
3. Ubah Pemain
4. Hapus Pemain
5. Keluar Program
""")
                pilih = input("Pilih menu (1-5): ")

                if pilih == "1":
                    print("\n=== TAMBAH PEMAIN ===")
                    nama = input("Nama: ")
                    umur = input("Umur: ")
                    tgl = input("Tanggal Lahir (dd-mm-yyyy): ")
                    tim = input("Tim: ")
                    jk = input("Jenis Kelamin (L/P): ")
                    data_pemain.append([nama, umur, tgl, tim, jk])
                    print("\nPemain berhasil ditambahkan!\n")

                elif pilih == "2":
                    print("\n=== DAFTAR PEMAIN ===")
                    nomor = 1
                    for p in data_pemain:
                        print(f"{nomor}. Nama          : {p[0]}")
                        print(f"   Umur          : {p[1]}")
                        print(f"   Tanggal Lahir : {p[2]}")
                        print(f"   Tim           : {p[3]}")
                        print(f"   Jenis Kelamin : {p[4]}")
                        print("-" * 30)
                        nomor += 1

                elif pilih == "3":
                    print("\n=== UBAH DATA PEMAIN ===")
                    for i in range(len(data_pemain)):
                        print(f"{i+1}. {data_pemain[i][0]} ({data_pemain[i][3]})")
                    nomor = int(input("Nomor pemain yang ingin diubah: "))
                    pemain = data_pemain[nomor - 1]
                    pemain[0] = input("Nama baru: ")
                    pemain[1] = input("Umur baru: ")
                    pemain[2] = input("Tanggal lahir baru: ")
                    pemain[3] = input("Tim baru: ")
                    pemain[4] = input("Jenis kelamin baru: ")
                    print("\nData pemain berhasil diperbarui!\n")

                elif pilih == "4":
                    print("\n=== HAPUS DATA PEMAIN ===")
                    for i in range(len(data_pemain)):
                        print(f"{i+1}. {data_pemain[i][0]} ({data_pemain[i][3]})")
                    nomor = int(input("Nomor pemain yang ingin dihapus: "))
                    hapus = data_pemain.pop(nomor - 1)
                    print(f"\nPemain {hapus[0]} berhasil dihapus!\n")

                elif pilih == "5":
                    print("\nTerima kasih!\n")
                    program_jalan = False
                    exit()

        elif role == "user":
            print("\nLogin berhasil sebagai USER\n")

            while True:
                print("""
==============================
    TIM ESPORT DATABASE 
          (USER)
==============================
1. Lihat Pemain
2. Keluar Program
""")
                pilih = input("Pilih menu (1-2): ")

                if pilih == "1":
                    print("\n=== DAFTAR PEMAIN ===")
                    nomor = 1
                    for p in data_pemain:
                        print(f"{nomor}. Nama          : {p[0]}")
                        print(f"   Umur          : {p[1]}")
                        print(f"   Tanggal Lahir : {p[2]}")
                        print(f"   Tim           : {p[3]}")
                        print(f"   Jenis Kelamin : {p[4]}")
                        print("-" * 30)
                        nomor += 1
                    print()

                elif pilih == "2":
                    print("\nTerima kasih!\n")
                    program_jalan = False
                    exit()

        else:
            print("\nLogin gagal! Username atau password salah.\n")

    elif menu_awal == "2":
        print("\n=== REGISTER ===")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")
        
       
        print("Pilih role:")
        print("1. Admin")
        print("2. User")
        pilih_role = input("Masukkan pilihan (1/2): ")

        if pilih_role == "1":
            role = "admin"
        else:
            role = "user"

        akun.append([username, password, role])
        print(f"\nRegistrasi berhasil sebagai {role}!\n")
