# auth.py

akun = {
    "admin": {"password": "admin123", "role": "admin"}
}

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
