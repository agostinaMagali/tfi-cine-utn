# --- VARIABLES GLOBALES DE CONTROL Y ESTADÍSTICAS ---
recaudacion_total = 0.0
total_entradas_vendidas = 0

# --- ESTRUCTURA DE DATOS PRINCIPAL (DICCIONARIO DE PELÍCULAS) ---
peliculas = {
    "1": ["Toy Story 5", 40, 0, 1500.0, "16:00 HS"],
    "2": ["Scary Movie 6", 30, 0, 1400.0, "22:30 HS"],
    "3": ["El Diablo Viste a la Moda 2", 35, 0, 1600.0, "19:00 HS"]
}

def validar_entero(mensaje) -> int:
    """Valida que el dato ingresado sea un número entero positivo mayor a cero."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("❌ Error: La cantidad debe ser un número entero mayor a cero.")
        except ValueError:
            print("❌ Error: Entrada inválida. Por favor, ingrese un número entero.")

def mostrar_cartelera():
    """Muestra en consola las películas cargadas con sus respectivos horarios y lugares disponibles."""
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

def realizar_reserva():
    """Gestiona el proceso completo de reserva de entradas, validaciones y cálculo con promociones."""
    global recaudacion_total, total_entradas_vendidas
    
    mostrar_cartelera()
    opcion_peli = input("\n👉 Seleccione el ID de la película que desea reservar: ").strip()
    
    if opcion_peli not in peliculas:
        print("❌ Error: El ID ingresado no corresponde a ninguna película en cartelera.")
        return

    nombre_peli, capacidad, ocupados, precio_base, horario = peliculas[opcion_peli]
    asientos_libres = capacidad - ocupados
    
    if asientos_libres == 0:
        print(f"❌ Lo sentimos. La sala para la función de '{nombre_peli}' está completamente llena.")
        return
        
    print(f"\n🎬 Película seleccionada: {nombre_peli} ({horario})")
    cant_entradas = validar_entero("🎟️ Ingrese la cantidad de entradas a reservar: ")
    
    if cant_entradas > asientos_libres:
        print(f"❌ Error: No se pueden reservar {cant_entradas} entradas. Solo quedan {asientos_libres} asientos disponibles.")
        return
        
    subtotal = cant_entradas * precio_base
    descuento = 0.0
    
    # Aplicación de Promoción (10% de descuento si se compran 3 o más entradas)
    if cant_entradas >= 3:
        descuento = subtotal * 0.10
        print(f"✨ ¡Promoción Activada! Se aplicó un 10% de descuento por compra de 3 o más entradas.")
        
    importe_final = subtotal - descuento
    
    # --- ACTUALIZACIÓN DE LAS VARIABLES GENERALES Y CONTADORES ---
    peliculas[opcion_peli][2] += cant_entradas  
    recaudacion_total += importe_final          
    total_entradas_vendidas += cant_entradas    
    
    # --- IMPRESIÓN DEL TICKET COMPROBANTE ---
    print("\n======================================")
    print("      🎟️ TICKET DE RESERVA EMITIDO 🎟️")
    print("======================================")
    print(f" Película:    {nombre_peli}")
    print(f" Horario:     {horario}")
    print(f" Cantidad:    {cant_entradas} entrada(s)")
    print(f" Subtotal:    ${subtotal:.2f}")
    print(f" Descuento:   ${descuento:.2f}")
    print(f" Total Pagar: ${importe_final:.2f}")
    print("======================================")
    print("✨ ¡Reserva guardada con éxito! Disfrute la función.")

def ver_estadisticas():
    """Genera reportes de gestión sobre ventas, recaudación y ocupación."""
    print("\n========================================================")
    print("📊          ESTADÍSTICAS GERENCIALES DEL CINE          ")
    print("========================================================")
    print(f"• Total de entradas vendidas hoy:   {total_entradas_vendidas}")
    print(f"• Recaudación total acumulada:      ${recaudacion_total:.2f}")
    print("--------------------------------------------------------")
    print("📈 Detalle de Ocupación por Película:")
    
    pelicula_mas_vista = "Ninguna"
    max_entradas = -1
    
    for id_peli, datos in peliculas.items():
        nombre, capacidad, ocupados, _, _ = datos
        porcentaje_ocupacion = (ocupados / capacidad) * 100
        print(f"  - {nombre:<28}: Ocupación del {porcentaje_ocupacion:.1f}% ({ocupados}/{capacidad})")
        
        if ocupados > max_entradas:
            max_entradas = ocupados
            pelicula_mas_vista = nombre
            
    print("--------------------------------------------------------")
    if total_entradas_vendidas > 0:
        print(f"🏆 Película con mayor demanda: {pelicula_mas_vista} ({max_entradas} entradas)")
    else:
        print("🏆 Película con mayor demanda: Aún no se registraron ventas hoy.")
    print("========================================================")

def menu_principal():
    """Controlador principal del ciclo de vida del programa en consola."""
    while True:
        print("\n======================================")
        print("   SISTEMA DE GESTIÓN DE CINE     ")
        print("======================================")
        print("1. Ver Cartelera de Películas")
        print("2. Registrar una Nueva Reserva")
        print("3. Ver Estadísticas y Reportes")
        print("4. Finalizar / Salir del Sistema")
        print("======================================")
        
        opcion = input("Seleccione una opción del menú (1-4): ").strip()
        
        if opcion == "1":
            mostrar_cartelera()
        elif opcion == "2":
            realizar_reserva()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            print("\n👋 Saliendo del sistema de simulación... ¡Buen día!")
            break
        else:
            print("❌ Opción no reconocida. Ingrese un número válido (1, 2, 3 o 4).")

# --- PUNTO DE ENTRADA AL PROGRAMA ---
if __name__ == "__main__":
    menu_principal()