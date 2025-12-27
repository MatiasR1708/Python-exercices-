import csv
from datetime import datetime

ARCHIVO = "espacios.csv"

def registrar_espacio():
    espacio = {
        "espacio_id": input("ID del espacio: "),
        "nombre_espacio": input("Nombre del espacio: "),
        "tipo": input("Tipo (AULA/LABORATORIO/SALA_ESPECIAL): "),
        "capacidad": input("Capacidad: "),
        "estado_actual": "DISPONIBLE",
        "fecha_registro": datetime.now().strftime("%Y-%m-%d")
    }

    with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=espacio.keys())
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(espacio)

    print("✅ Espacio registrado correctamente")

def listar_espacios():
    with open(ARCHIVO, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("\nID | Nombre | Tipo | Capacidad | Estado")
        for e in reader:
            print(e["espacio_id"], e["nombre_espacio"], e["tipo"], e["capacidad"], e["estado_actual"])

def obtener_espacio(espacio_id):
    espacios = []
    encontrado = None

    with open(ARCHIVO, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for e in reader:
            espacios.append(e)
            if e["espacio_id"] == espacio_id:
                encontrado = e

    return espacios, encontrado

def actualizar_espacios(lista):
    if not lista:
        return

    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=lista[0].keys())
        writer.writeheader()
        writer.writerows(lista)
