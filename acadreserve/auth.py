import csv

def login():
    intentos = 3

    while intentos > 0:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        try:
            with open("usuarios.csv", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for fila in reader:
                    if fila["usuario"] == usuario and fila["contrasena"] == contrasena:
                        print("✅ Acceso concedido\n")
                        return True
        except FileNotFoundError:
            print("❌ No se encuentra usuarios.csv")
            return False

        intentos -= 1
        print(f"❌ Credenciales incorrectas. Intentos restantes: {intentos}")

    print("🚫 Máximo de intentos alcanzado. Programa finalizado.")
    return False
