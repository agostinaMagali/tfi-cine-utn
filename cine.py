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
            print("❌ Error: La cantidad debe ser mayor a cero.")
        except ValueError:
            print("❌ Error: Entrada inválida. Ingrese un número entero.")

def mostrar_cartelera():
    print("\n==========================================================================")
    print("🎬                      CARTELERA DE FUNCIONES                           ")
    print("==========================================================================")
    for id_peli, datos in peliculas.items():
        nombre, capacidad, ocupados, precio, horario = datos
        disponibles = capacidad - ocupados
        print(f"[{id_peli}]  | {nombre:<30} | {horario:<10} | ${precio:<9.2f} | {disponibles}/{capacidad} asientos")

def realizar_reserva():
    global recaudacion_total, total_entradas_vendidas
    mostrar_cartelera()
    opcion_peli = input("\n👉 Seleccione el ID de la película que desea reservar: ").strip()
    
    if opcion_peli not in peliculas:
        print("❌ Error: El ID ingresado no es válido.")
        return

    nombre_peli, capacidad, ocupados, precio_base, horario = peliculas[opcion_peli]
    asientos_libres = capacidad - ocupados
    
    if asientos_libres == 0:
        print("❌ Lo sentimos. Sala llena.")
        return
        
    print(f"\n🎬 Película seleccionada: {nombre_peli}")
    cant_entradas = validar_entero("🎟️ Ingrese la cantidad de entradas: ")
    
    if cant_entradas > asientos_libres:
        print(f"❌ Error: Solo quedan {asientos_libres} asientos disponibles.")
        return
        
    subtotal = cant_entradas * precio_base
    descuento = subtotal * 0.10 if cant_entradas >= 3 else 0.0
    importe_final = subtotal - descuento
    
    peliculas[opcion_peli][2] += cant_entradas  
    recaudacion_total += importe_final          
    total_entradas_vendidas += cant_entradas    
    print(f"\n🎟️ TICKET EMITIDO - Total a pagar: ${importe_final:.2f}")

def menu_principal():
    while True:
        print("\n======================================")
        print("   SISTEMA DE GESTIÓN DE CINE v2.0    ")
        print("======================================")
        print("1. Ver Cartelera de Películas")
        print("2. Registrar una Nueva Reserva")
        print("3. Ver Estadísticas (Próximamente)")
        print("4. Finalizar / Salir del Sistema")
        print("======================================")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "1": mostrar_cartelera()
        elif opcion == "2": realizar_reserva()
        elif opcion == "4": break

if __name__ == "__main__":
    menu_principal()