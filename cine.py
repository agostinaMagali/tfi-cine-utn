def menu_principal():
    while True:
        print("\n======================================")
        print("   SISTEMA DE GESTIÓN DE CINE v2.0    ")
        print("======================================")
        print("1. Ver Cartelera de Películas")
        print("2. Registrar una Nueva Reserva")
        print("3. Ver Estadísticas y Reportes")
        print("4. Finalizar / Salir del Sistema")
        print("======================================")
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "4":
            print("👋 ¡Gracias por usar el sistema!")
            break

if __name__ == "__main__":
    menu_principal()