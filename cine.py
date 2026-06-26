# VARIABLES GLOBALES DE CONTROL Y ESTADÍSTICAS
recaudacion_total = 0.0
total_entradas_vendidas = 0

# ESTRUCTURA DE DATOS PRINCIPAL (DICCIONARIO DE PELÍCULAS)
peliculas = {
    "1": ["Toy Story 5", 40, 0, 1500.0, "16:00 HS"],
    "2": ["Scary Movie 6", 30, 0, 1400.0, "22:30 HS"],
    "3": ["El Diablo Viste a la Moda 2", 35, 0, 1600.0, "19:00 HS"]
}

def mostrar_cartelera():
    print("\n==========================================================================")
    print("🎬                      CARTELERA DE FUNCIONES                           ")
    print("==========================================================================")
    print(f"{'ID':<4} | {'Película':<30} | {'Horario':<10} | {'Precio':<10} | {'Disponibilidad'}")
    print("--------------------------------------------------------------------------")
    for id_peli, datos in peliculas.items():
        nombre, capacidad, ocupados, precio, horario = datos
        disponibles = capacidad - ocupados
        print(f"[{id_peli}]  | {nombre:<30} | {horario:<10} | ${precio:<9.2f} | {disponibles}/{capacidad} asientos")
    print("==========================================================================")

def menu_principal():
    while True:
        print("\n======================================")
        print("   SISTEMA DE GESTIÓN DE CINE v2.0    ")
        print("======================================")
        print("1. Ver Cartelera de Películas")
        print("2. Registrar una Nueva Reserva (Próximamente)")
        print("3. Ver Estadísticas (Próximamente)")
        print("4. Finalizar / Salir del Sistema")
        print("======================================")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "1":
            mostrar_cartelera()
        elif opcion == "4":
            print("\n👋 ¡Gracias por usar el sistema!")
            break

if __name__ == "__main__":
    menu_principal()