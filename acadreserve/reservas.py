import csv
import json
from datetime import datetime
from espacios import obtener_espacio, actualizar_espacios

ARCHIVO = "reservas.csv"

def cargar_limites():
    with open("configuracion.json", encoding="utf-8") as f:
        data = json.load(f)
    return data["limites_por_tipo"]

def solicitar_reserva():
    espacio_id = input("ID del espacio: ")
    espacios, espacio = obtener_espacio(espacio_id)

    if not espacio or espacio["estado_actual"] != "DISPONIBLE":
        print("❌ El espacio no está disponible")
        return

    nombre = input("Nombre del solicitante: ")
    tipo_usuario = input("Tipo (ESTUDIANTE/DOCENTE/ADMINISTRATIVO): ")
    fecha_reserva = input("Fecha reserva (YYYY-MM-DD): ")
    horas = int(input("Horas solicitadas: "))

    limites = cargar_limites()
    if horas > limites[tipo_usuario]:
        print("❌ Excede el límite permitido")
        return

    reserva = {
        "reserva_id": datetime.now().strftime("%H%M%S"),
        "espacio_id": espacio_id,
        "nombre_espacio": espacio["nombre_espacio"],
        "usuario_reservante": nombre,
        "tipo_usuario": tipo_usuario,
        "fecha_solicitud": datetime.now().strftime("%Y-%m-%d"),
        "fecha_reserva": fecha_reserva,
        "horas_autorizadas": horas,
        "horas_reales_usadas": "",
        "exceso_tiempo": "",
        "estado": "PENDIENTE",
        "mes": str(datetime.now().month),
        "anio": str(datetime.now().year)
    }

    with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=reserva.keys())
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(reserva)

    print("✅ Reserva registrada como PENDIENTE")

def aprobar_reserva():
    reservas = []

    with open(ARCHIVO, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            reservas.append(r)

    pendientes = [r for r in reservas if r["estado"] == "PENDIENTE"]

    if not pendientes:
        print("No hay reservas pendientes")
        return

    for i, r in enumerate(pendientes):
        print(i, r["reserva_id"], r["nombre_espacio"])

    op = int(input("Seleccione una reserva: "))
    pendientes[op]["estado"] = "APROBADA"

    espacios, espacio = obtener_espacio(pendientes[op]["espacio_id"])
    espacio["estado_actual"] = "RESERVADO"
    actualizar_espacios(espacios)

    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=reservas[0].keys())
        writer.writeheader()
        writer.writerows(reservas)

    print("✅ Reserva aprobada")

def finalizar_reserva():
    reservas = []

    with open(ARCHIVO, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            reservas.append(r)

    aprobadas = [r for r in reservas if r["estado"] == "APROBADA"]

    if not aprobadas:
        print("No hay reservas aprobadas")
        return

    for i, r in enumerate(aprobadas):
        print(i, r["reserva_id"], r["nombre_espacio"])

    op = int(input("Seleccione una reserva: "))
    inicio = float(input("Hora inicio real: "))
    fin = float(input("Hora fin real: "))

    usadas = fin - inicio
    aprobadas[op]["horas_reales_usadas"] = usadas
    aprobadas[op]["exceso_tiempo"] = "SI" if usadas > float(aprobadas[op]["horas_autorizadas"]) else "NO"
    aprobadas[op]["estado"] = "FINALIZADA"

    espacios, espacio = obtener_espacio(aprobadas[op]["espacio_id"])
    espacio["estado_actual"] = "DISPONIBLE"
    actualizar_espacios(espacios)

    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=reservas[0].keys())
        writer.writeheader()
        writer.writerows(reservas)

    print("✅ Reserva finalizada")
