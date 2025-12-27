import csv

def exportar_reporte():
    mes = input("Mes: ")
    anio = input("Año: ")
    nombre = f"reporte_reservas_{anio}_{mes}.csv"

    encontrado = False

    with open("reservas.csv", newline="", encoding="utf-8") as f, \
         open(nombre, "w", newline="", encoding="utf-8") as out:

        reader = csv.DictReader(f)
        writer = csv.DictWriter(out, fieldnames=reader.fieldnames)
        writer.writeheader()

        for r in reader:
            if r["estado"] == "FINALIZADA" and r["mes"] == mes and r["anio"] == anio:
                writer.writerow(r)
                encontrado = True

    if encontrado:
        print(f"✅ Reporte generado: {nombre}")
    else:
        print("❌ No hay datos para ese período")
