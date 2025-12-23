# CREAR CONTRASEÑA
while True:
    CorrectPassword = input("Crea una contraseña (más de 8 caracteres, sin espacios): ")

    if len(CorrectPassword) > 8 and " " not in CorrectPassword:
        print("Contraseña creada correctamente\n")
        break
    else:
        print("La contraseña no cumple las reglas\n")

# LOGIN CON INTENTOS LIMITADOS
intentos = 3
acceso = False   # bandera de control

while intentos > 0:
    Password = input("Ingrese la contraseña: ")

    if Password == CorrectPassword:
        print("Acceso concedido")
        acceso = True
        break
    else:
        intentos -= 1
        print("Acceso denegado")

        if intentos > 0:
            print(f"Te quedan {intentos} intentos")

if not acceso:
    print("Superaste los intentos permitidos")
    exit()   # 👈 CIERRA TODO EL PROGRAMA