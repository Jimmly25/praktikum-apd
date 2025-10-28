akun = {"admin": {"password": "admin123", "role": "admin"}}
data_pemain = {}
program_jalan = True



def tampilkan_menu_awal():
    print("""
==============================
     SISTEM LOGIN ESPORT
==============================
1. Login
2. Register
3. Keluar Program
""")


def tampilkan_menu_admin():
    print("""
=== MENU ADMIN ===
1. Tambah Pemain
2. Lihat Pemain
3. Ubah Pemain
4. Hapus Pemain
5. Keluar Program
""")


def tampilkan_menu_user():
    print("""
=== MENU USER ===
1. Lihat Pemain
2. Keluar
""")



def login(username, password):
    if username in akun and akun[username]["password"] == password:
        return akun[username]["role"]
    return None


def register(username, password, role):
    if username in akun:
        print("Username sudah digunakan!")
        return
    akun[username] = {"password": password, "role": role}
    print(f"Registrasi berhasil sebagai {role}!")



def tambah_pemain():

    while True:
        nama = input("Nama: ")
        if not nama:
            print(" Nama tidak boleh kosong! Coba lagi.")
            continue
       
        if nama in data_pemain:
            print(" Nama pemain sudah terdaftar! Gunakan nama lain.")
            continue
        break

    
    while True:
        umur_input = input("Umur: ")
        if not umur_input:
            print(" Umur tidak boleh kosong! Coba lagi.")
            continue
        try:
            umur = int(umur_input)
            if umur <= 0:
                print(" Umur harus lebih dari 0! Coba lagi.")
                continue
            break
        except ValueError:
            print(" Umur harus berupa angka! Coba lagi.")

    
    while True:
        tgl = input("Tanggal lahir (dd-mm-yyyy): ")
        if not tgl:
            print(" Tanggal lahir tidak boleh kosong! Gunakan format dd-mm-yyyy.")
            continue
        if any(char.isalpha() for char in tgl):
            print(" Tanggal lahir tidak boleh mengandung huruf!")
            continue
        bagian = tgl.split("-")
        if len(bagian) != 3 or not all(b.isdigit() for b in bagian):
            print(" Format tanggal salah! Gunakan format dd-mm-yyyy.")
            continue
        break
   
    while True:
        tim = input("Tim: ")
        if not tim:
            print(" Nama tim tidak boleh kosong! Coba lagi.")
        else:
            break

  
    while True:
        jk = input("Jenis kelamin (L/P): ").upper()
        if jk not in ["L", "P"]:
            print(" Jenis kelamin harus 'L' atau 'P'! Coba lagi.")
        else:
            break

 
    data_pemain[nama] = {"umur": umur, "tgl": tgl, "tim": tim, "jk": jk}
    print("\n Pemain berhasil ditambahkan!\n")


def lihat_pemain():
    if not data_pemain:
        print("Belum ada pemain.\n")
    else:
        print("\n=== DAFTAR PEMAIN ===")
        for nama, p in data_pemain.items():
            print(f"\nNama          : {nama}")
            print(f"Umur          : {p['umur']}")
            print(f"Tanggal Lahir : {p['tgl']}")
            print(f"Tim           : {p['tim']}")
            print(f"Jenis Kelamin : {p['jk']}")
            print("-" * 30)
        print()


def ubah_pemain():
    nama_lama = input("Masukkan nama pemain yang ingin diubah: ")
    if nama_lama in data_pemain:
        nama_baru = input("Nama baru (Enter jika tidak diubah): ") or nama_lama

     
        while True:
            umur_baru = input("Umur baru (Enter jika tidak diubah): ")
            if umur_baru == "":
                umur_baru = data_pemain[nama_lama]["umur"]
                break
            try:
                umur_baru = int(umur_baru)
                break
            except ValueError:
                print("Umur harus berupa angka! Coba lagi.")

        
        while True:
            tgl_baru = input("Tanggal lahir baru (Enter jika tidak diubah): ")
            if tgl_baru == "":
                tgl_baru = data_pemain[nama_lama]["tgl"]
                break
            if any(char.isalpha() for char in tgl_baru):
                print("Tanggal lahir tidak boleh mengandung huruf! Gunakan format dd-mm-yyyy.")
                continue
            bagian = tgl_baru.split("-")
            if len(bagian) != 3 or not all(b.isdigit() for b in bagian):
                print("Format tanggal salah! Gunakan format dd-mm-yyyy.")
                continue
            break

        tim_baru = input("Tim baru (Enter jika tidak diubah): ") or data_pemain[nama_lama]["tim"]
        jk_baru = input("Jenis kelamin baru (Enter jika tidak diubah): ").upper() or data_pemain[nama_lama]["jk"]

        if jk_baru not in ["L", "P"]:
            print("Jenis kelamin harus 'L' atau 'P'!")
            jk_baru = data_pemain[nama_lama]["jk"]

  
        if nama_baru != nama_lama:
            data_pemain[nama_baru] = data_pemain.pop(nama_lama)

        data_pemain[nama_baru] = {
            "umur": umur_baru,
            "tgl": tgl_baru,
            "tim": tim_baru,
            "jk": jk_baru
        }
        print(" Data pemain berhasil diperbarui!\n")
    else:
        print(" Nama tidak ditemukan!\n")


def hapus_pemain():
    nama = input("Masukkan nama pemain yang ingin dihapus: ")
    if nama in data_pemain:
        del data_pemain[nama]
        print(f" Pemain '{nama}' berhasil dihapus.\n")
    else:
        print(" Nama tidak ditemukan.\n")



while program_jalan:
    tampilkan_menu_awal()
    pilih_awal = input("Pilih menu: ")

    if pilih_awal == "1":  
        user = input("Username: ")
        pw = input("Password: ")
        role = login(user, pw)

        if role == "admin":
            print("Login sebagai ADMIN berhasil!\n")
            while True:
                tampilkan_menu_admin()
                pilih = input("Pilih menu: ")

                if pilih == "1":
                    tambah_pemain()
                elif pilih == "2":
                    lihat_pemain()
                elif pilih == "3":
                    ubah_pemain()
                elif pilih == "4":
                    hapus_pemain()
                elif pilih == "5":
                    print("Terima Kasih.\n")
                    program_jalan = False
                    break
                else:
                    print("Pilihan tidak valid!\n")

        elif role == "user":
            print("Login sebagai USER berhasil!\n")
            while True:
                tampilkan_menu_user()
                pilih = input("Pilih menu: ")

                if pilih == "1":
                    lihat_pemain()
                elif pilih == "2":
                  
                    break  
                else:
                    print("Pilihan tidak valid!\n") 

        else:
            print(" Login gagal! Username atau password salah.\n")

    elif pilih_awal == "2":  
        username = input("Buat Username: ")
        if username in akun:
            print(" Username sudah digunakan!\n")
            continue
        password = input("Buat Password: ")
        role = input("Daftar sebagai (admin/user): ")
        if role not in ["admin", "user"]:
            print(" Role tidak valid!\n")
            continue
        register(username, password, role)

    elif pilih_awal == "3": 
        print("Terima kasih telah menggunakan Sistem Login Esport!\n")
        program_jalan = False

    else:
        print(" Pilihan tidak valid!\n")
