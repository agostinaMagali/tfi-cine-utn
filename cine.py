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

    recaudacion_total = 0.0
total_entradas_vendidas = 0

peliculas = {
    "1": ["Toy Story 5", 40, 0, 1500.0, "16:00 HS"],
    "2": ["Scary Movie 6", 30, 0, 1400.0, "22:30 HS"],
    "3": ["El Diablo Viste a la Moda 2", 35, 0, 1600.0, "19:00 HS"]
}

def validar_entero(mensaje) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0: return valor
            print("❌ Error: Debe ser mayor a cero.")
        except ValueError:
            print("❌ Error: Ingrese un número entero.")

def mostrar_cartelera():
    print("\n🎬 --- CARTELERA ---")
    for id_peli, datos in peliculas.items():
        nombre, cap, ocup, prec, hor = datos
        print(f"[{id_peli}] {nombre:<30} | {hor} | ${prec}")

