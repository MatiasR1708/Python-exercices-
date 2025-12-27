from auth import login
import espacios
import reservas
import reportes

if login():
    while True:
        print("""
====== ACADRESERVE ======
1. Registrar espacio
2. Listar espacios
3. Solicitar reserva
4. Aprobar reserva
5. Finalizar reserva
6. Exportar reporte
7. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            espacios.registrar_espacio()
        elif opcion == "2":
            espacios.listar_espacios()
        elif opcion == "3":
            reservas.solicitar_reserva()
        elif opcion == "4":
            reservas.aprobar_reserva()
        elif opcion == "5":
            reservas.finalizar_reserva()
        elif opcion == "6":
            reportes.exportar_reporte()
        elif opcion == "7":
            print("👋 Saliendo del sistema")
            break
        else:
            print("❌ Opción inválida")
