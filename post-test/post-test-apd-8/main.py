
from auth import login, register, akun
from menu import tampilkan_menu_awal, tampilkan_menu_admin, tampilkan_menu_user
from pemain import tambah_pemain, lihat_pemain, ubah_pemain, hapus_pemain

program_jalan = True

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
            print("Login gagal! Username atau password salah.\n")

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
        print("Pilihan tidak valid!\n")
