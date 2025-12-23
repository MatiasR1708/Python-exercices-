CorrectPassword = "python123"
intentos = 3

while intentos > 0:
    Password = input("Ingrese la contraseña: ")

    if Password == CorrectPassword:
        print("Acceso concedido")
        break
    else:
        intentos -= 1
        print("Acceso denegado")

        if intentos > 0:
            print(f"Te quedan {intentos} intentos")

if intentos == 0:
    print("Superaste los intentos permitidos")
