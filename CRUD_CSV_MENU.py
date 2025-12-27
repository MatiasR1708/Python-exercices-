import csv
import os

ARCHIVO = "datos.csv"

# =========================
# FUNCIONES DE ARCHIVO
# =========================

def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return []

    datos = []
    with open(ARCHIVO, "r", newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            datos.append(fila)

    return datos


def guardar_datos(datos):
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        campos = ["nombre", "categoria", "valor"]
        escritor = csv.DictWriter(f, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(datos)

# =========================
# FUNCIONES DEL MENÚ
# =========================

def agregar_registro(datos):
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    valor = input("Valor: ")

    registro = {
        "nombre": nombre,
        "categoria": categoria,
        "valor": valor
    }

    datos.append(registro)
    guardar_datos(datos)
    print("Registro agregado correctamente")


def mostrar_registros(datos):
    if not datos:
        print("No hay registros")
        return

    for i, registro in enumerate(datos, start=1):
        print(f"\nRegistro {i}")
        for clave, valor in registro.items():
            print(f"{clave}: {valor}")


def actualizar_registro(datos):
    mostrar_registros(datos)

    try:
        indice = int(input("\nNúmero de registro a actualizar: ")) - 1

        if indice < 0 or indice >= len(datos):
            print("Registro no válido")
            return

        registro = datos[indice]

        print("\nDeja en blanco si no deseas cambiar el valor")

        nuevo_nombre = input(f"Nuevo nombre ({registro['nombre']}): ")
        nueva_categoria = input(f"Nueva categoría ({registro['categoria']}): ")
        nuevo_valor = input(f"Nuevo valor ({registro['valor']}): ")

        if nuevo_nombre:
            registro["nombre"] = nuevo_nombre
        if nueva_categoria:
            registro["categoria"] = nueva_categoria
        if nuevo_valor:
            registro["valor"] = nuevo_valor

        guardar_datos(datos)
        print("Registro actualizado correctamente")

    except:
        print("Opción inválida")


def eliminar_registro(datos):
    mostrar_registros(datos)

    try:
        indice = int(input("\nNúmero de registro a eliminar: ")) - 1
        eliminado = datos.pop(indice)
        guardar_datos(datos)
        print(f"Registro eliminado: {eliminado['nombre']}")
    except:
        print("Opción inválida")

# =========================
# MENÚ PRINCIPAL
# =========================

def menu():
    datos = cargar_datos()

    while True:
        print("\n--- MENÚ GENERAL ---")
        print("1. Agregar registro")
        print("2. Mostrar registros")
        print("3. Actualizar registro")
        print("4. Eliminar registro")
        print("5. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_registro(datos)
        elif opcion == "2":
            mostrar_registros(datos)
        elif opcion == "3":
            actualizar_registro(datos)
        elif opcion == "4":
            eliminar_registro(datos)
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida")


menu()
