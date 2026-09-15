# Lista de 2 dimensiones: [Código, Denominación, Stock]
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

# Diccionario de empleados: {Legajo: "Nombre y Apellido"}
empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

# Tupla de claves de técnico (3 palabras en orden)
claves_tecnico = ("admin", "CCCDDD", "2020")

# Lista vacía para guardar el historial de pedidos
golosinas_pedidas = []

while True:
    print("\n--- MAQUINA DE GOLOSINAS ---")
    print("a. Pedir golosina")
    print("b. Mostrar golosinas")
    print("c. Rellenar golosinas")
    print("d. Apagar maquina")

    # Capturamos la opción elegida y la pasamos a minúsculas
    opcion = input("Elija una opción (a, b, c, d): ").lower()

    # Opción a: Proceso para pedir una golosina
    if opcion == 'a':
        # Validar que el legajo ingresado sea un número entero
        try:
            legajo_ingresado = int(input("Ingrese su legajo de empleado: "))
        except ValueError:
            print("Por favor, ingrese un número de legajo válido.")
            continue

        # Verificar si el legajo existe en nuestro diccionario de empleados    
        if legajo_ingresado not in empleados:
            print("Usted no es un empleado de la empresa")
        else:
            print(f"¡Bienvenido, {empleados[legajo_ingresado]}!")

            # Pedimos el código numérico de la golosina deseada
            try:
                codigo_golosina = int(input("Ingrese el código de la golosina que desea: "))
            except ValueError:
                print("Por favor, ingrese un código numérico válido.")
                continue

            # Buscamos la golosina dentro de la lista bidimensional
            golosina_encontrada = None
            for g in golosinas:
                if g[0] == codigo_golosina:
                    golosina_encontrada = g
                    break

            # Controlamos si el código ingresado existe realmente
            if golosina_encontrada is None:
                print("El código de golosina ingresado no existe.")
            else:
                nombre_golosina = golosina_encontrada[1]
                stock_actual = golosina_encontrada[2]

                # Comprobamos si hay stock disponible (mayor a 0)
                if stock_actual > 0:
                    golosina_encontrada[2] -= 1
                    print(f"¡Disfrute su {nombre_golosina}!")

                    # Registramos el pedido en el historial o sumamos cantidad si ya estaba
                    en_historial = False
                    for item in golosinas_pedidas:
                        if item[0] == codigo_golosina:
                            item[2] += 1
                            en_historial = True
                            break
                    
                    if not en_historial:
                        golosinas_pedidas.append([codigo_golosina, nombre_golosina, 1])
                else:
                    # Si no hay stock, permitimos elegir otro código o salir
                    while True:
                        print(f"Lo sentimos la golosina {nombre_golosina} no se encuentra disponible")
                        opcion_stock = input("Seleccione otra golosina (ingrese el código) o ingrese 'salir' si no desea otra: ").lower()
                        
                        if opcion_stock == 'salir':
                            print("Operación cancelada.")
                            break
                        else:
                            try:
                                nuevo_codigo = int(opcion_stock)
                                otra_golosina = None
                                for g in golosinas:
                                    if g[0] == nuevo_codigo:
                                        otra_golosina = g
                                        break
                                
                                if otra_golosina is not None and otra_golosina[2] > 0:
                                    otra_golosina[2] -= 1
                                    print(f"¡Disfrute su {otra_golosina[1]}!")
                                    
                                    en_historial = False
                                    for item in golosinas_pedidas:
                                        if item[0] == nuevo_codigo:
                                            item[2] += 1
                                            en_historial = True
                                            break
                                    if not en_historial:
                                        golosinas_pedidas.append([nuevo_codigo, otra_golosina[1], 1])
                                    break
                                else:
                                    print("Código inválido o también sin stock. Intente nuevamente.")
                            except ValueError:
                                print("Entrada inválida. Ingrese un número de código o la palabra 'salir'.")

    # Opción b: Mostrar el stock actual de golosinas en pantalla
    elif opcion == 'b':
        print("\n--- STOCK ACTUAL DE GOLOSINAS --")
        print("Código | Denominación | Stock")
        print("-" * 35)
        for g in golosinas:
            print(f"{g[0]:<6} | {g[1]:<18} | {g[2]}")

    # Opción c: Panel técnico para recargar stock con credenciales
    elif opcion == 'c':
        print("\n--- PANEL DE TÉCNICO ---")
        p1 = input("Ingrese la palabra clave 1: ")
        p2 = input("Ingrese la palabra clave 2: ")
        p3 = input("Ingrese la palabra clave 3: ")

        # Validamos las credenciales contra la secuencia de claves permitidas
        if (p1, p2, p3) == claves_tecnico:
            print("Acceso autorizado.")
            try:
                codigo_recarga = int(input("Ingrese el código de la golosina a rellenar: "))
                cantidad_recarga = int(input("Ingrese la cantidad a recargar (mayor a 0): "))
                
                if cantidad_recarga > 0:
                    encontrado_tecnico = False
                    for g in golosinas:
                        if g[0] == codigo_recarga:
                            g[2] += cantidad_recarga
                            print(f"Stock actualizado de {g[1]}. Nuevo stock: {g[2]}")
                            encontrado_tecnico = True
                            break
                    if not encontrado_tecnico:
                        print("El código de golosina no existe.")
                else:
                    print("La cantidad debe ser mayor a cero.")
            except ValueError:
                print("Error: Debe ingresar valores numéricos válidos.")
        else:
            print("No tiene permiso para ejecutar la función de recarga")

    # Opción d: Apagar la máquina, mostrar historial y sumar totales
    elif opcion == 'd':
        print("\n--- HISTORIAL DE GOLOSINAS PEDIDAS ---")
        if not golosinas_pedidas:
            print("No se pidieron golosinas durante la ejecución.")
        else:
            print("Código | Denominación       | Cantidad Pedida")
            print("-" * 45)
            total_general = 0
            for item in golosinas_pedidas:
                print(f"{item[0]:<6} | {item[1]:<18} | {item[2]}")
                total_general += item[2]
            print("-" * 45)
            print(f"TOTAL GENERAL DE GOLOSINAS PEDIDAS: {total_general}")
            
        print("Apagando máquina...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

