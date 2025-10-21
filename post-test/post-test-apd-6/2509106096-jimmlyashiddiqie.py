
akun = {
    "admin": {"password": "admin123", "role": "admin"}
}


data_pemain = {}

menu_awal = {
    "1": "Login",
    "2": "Register"
}

menu_admin = {
    "1": "Tambah Pemain",
    "2": "Lihat Pemain",
    "3": "Ubah Pemain",
    "4": "Hapus Pemain",
    "5": "Keluar Program"
}

menu_user = {
    "1": "Lihat Pemain",
    "2": "Keluar Program"
}

pilihan_role = {
    "1": "admin",
    "2": "user"
}

program_jalan = True

while program_jalan:
    print("""
==============================
     SISTEM LOGIN ESPORT
==============================""")
    
    for key, value in menu_awal.items():
        print(f"{key}. {value}")
    pilih_awal = input("Pilih menu: ")

   
    if pilih_awal == "1":
        user = input("Username: ")
        pw = input("Password: ")

        if user in akun and akun[user]["password"] == pw:
            role = akun[user]["role"]

     
            if role == "admin":
                print("Login sebagai ADMIN berhasil!")
                while True:
                    print("\n=== MENU ADMIN ===")
                    for k, v in menu_admin.items():
                        print(f"{k}. {v}")
                    pilih = input("Pilih menu: ")

               
                    if pilih == "1":
                        nama = input("Nama: ")
                        umur = input("Umur: ")
                        tgl = input("Tanggal lahir (dd-mm-yyyy): ")
                        tim = input("Tim: ")
                        jk = input("Jenis kelamin (L/P): ")
                        data_pemain[nama] = {"umur": umur, "tgl": tgl, "tim": tim, "jk": jk}
                        print("Pemain berhasil ditambahkan!")

            
                    elif pilih == "2":
                        if not data_pemain:
                            print("Belum ada pemain.")
                        else:
                            print("\n=== DAFTAR PEMAIN ===")
                            for nama, p in data_pemain.items():
                                print(f"\nNama          : {nama}")
                                print(f"Umur          : {p['umur']}")
                                print(f"Tanggal Lahir : {p['tgl']}")
                                print(f"Tim           : {p['tim']}")
                                print(f"Jenis Kelamin : {p['jk']}")
                                print("-" * 30)

                    elif pilih == "3":
                        nama_lama = input("Masukkan nama pemain yang ingin diubah: ")
                        if nama_lama in data_pemain:
                        
                            nama_baru = input("Nama baru: ") or nama_lama
                            umur_baru = input("Umur baru: ") or data_pemain[nama_lama]["umur"]
                            tgl_baru = input("Tanggal lahir baru: ") or data_pemain[nama_lama]["tgl"]
                            tim_baru = input("Tim baru: ") or data_pemain[nama_lama]["tim"]
                            jk_baru = input("Jenis kelamin baru (L/P): ") or data_pemain[nama_lama]["jk"]

                            if nama_baru != nama_lama:
                                data_pemain[nama_baru] = data_pemain.pop(nama_lama)

                            data_pemain[nama_baru] = {
                                "umur": umur_baru,
                                "tgl": tgl_baru,
                                "tim": tim_baru,
                                "jk": jk_baru
                            }
                            print("Data pemain berhasil diperbarui!")
                        else:
                            print("Nama tidak ditemukan!")

                 
                    elif pilih == "4":
                        nama = input("Masukkan nama pemain yang ingin dihapus: ")
                        if nama in data_pemain:
                            del data_pemain[nama]
                            print(f"Pemain '{nama}' berhasil dihapus!")
                        else:
                            print("Nama tidak ditemukan!")

                    
                    elif pilih == "5":
                        print("Keluar dari program.")
                        program_jalan = False
                        break

      
            else:
                print("Login sebagai USER berhasil!")
                while True:
                    print("\n=== MENU USER ===")
                    for k, v in menu_user.items():
                        print(f"{k}. {v}")
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        if not data_pemain:
                            print("Belum ada pemain.")
                        else:
                            print("\n=== DAFTAR PEMAIN ===")
                            for nama, p in data_pemain.items():
                                print(f"\nNama          : {nama}")
                                print(f"Umur          : {p['umur']}")
                                print(f"Tanggal Lahir : {p['tgl']}")
                                print(f"Tim           : {p['tim']}")
                                print(f"Jenis Kelamin : {p['jk']}")
                                print("-" * 30)

                    elif pilih == "2":
                        print("Terima kasih!")
                        program_jalan = False
                        break

        else:
            print("Login gagal! Username atau password salah")

    
    elif pilih_awal == "2":
        username = input("Buat Username: ")
        password = input("Buat Password: ")
        print("Pilih role:")
        for key, value in pilihan_role.items():
            print(f"{key}. {value}")
        pilih_role = input("Masukkan pilihan: ")
        role = pilihan_role.get(pilih_role, "user")
        akun[username] = {"password": password, "role": role}
        print(f"Registrasi berhasil sebagai {role}!")

    else:
        print("Pilihan tidak valid!")
