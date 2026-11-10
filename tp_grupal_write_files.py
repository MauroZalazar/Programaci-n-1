import os

def leer_alumnos(archivo="alumnos.txt") -> list[str]:
    if not os.path.exists(archivo):
        with open(archivo, "w", encoding="utf-8") as f:
            pass
        return []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return [linea.strip() for linea in f.readlines() if linea.strip()]
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

def generar_diccionario_alumnos(lineas: list[str]) -> dict:
    diccionario = {}
    for linea in lineas:
        partes = [p.strip() for p in linea.split(";")]
        if len(partes) == 4:
            nombre, apellido, legajo, nota = partes
            diccionario[legajo] = {
                "nombre": nombre,
                "apellido": apellido,
                "nota": float(nota)
            }
    return diccionario

def validar_existe_alumno(legajo: str, diccionario: dict) -> bool:
    if legajo in diccionario:
        print(f"El legajo {legajo} ya existe en el archivo alumnos.txt, no se permite su escritura")
        return True
    return False

def agregar_alumno(archivo="alumnos.txt"):
    lineas = leer_alumnos(archivo)
    diccionario = generar_diccionario_alumnos(lineas)
    
    while True:
        nombre = input("Ingrese nombre (solo letras): ").strip()
        if nombre.isalpha():
            break
        print("Error: El nombre solo debe contener letras.")

    while True:
        apellido = input("Ingrese apellido (solo letras): ").strip()
        if apellido.isalpha():
            break
        print("Error: El apellido solo debe contener letras.")

    while True:
        legajo = input("Ingrese legajo (5 dígitos): ").strip()
        if legajo.isdigit() and len(legajo) == 5:
            if not validar_existe_alumno(legajo, diccionario):
                break
        else:
            print("Error: El legajo debe tener exactamente 5 dígitos numéricos.")

    while True:
        try:
            nota_str = input("Ingrese nota promedio (entre 1 y 10): ").strip()
            nota = float(nota_str)
            if 1 <= nota <= 10:
                break
            print("Error: La nota debe estar entre 1 y 10.")
        except ValueError:
            print("Error: Debe ingresar un valor numérico.")

    nueva_linea = f"{nombre}; {apellido}; {legajo}; {int(nota) if nota.is_integer() else nota}\n"
    
    try:
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(nueva_linea)
        print("Alumno agregado exitosamente.")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def ver_alumnos(archivo="alumnos.txt"):
    lineas = leer_alumnos(archivo)
    if not lineas:
        print("El archivo de alumnos está vacío.")
        return
    print("\n--- LISTA DE ALUMNOS ---")
    for linea in lineas:
        partes = [p.strip() for p in linea.split(";")]
        if len(partes) == 4:
            nombre, apellido, legajo, nota = partes
            print(f"Alumno: {nombre} {apellido} | Legajo: {legajo} | Promedio: {nota}")
    print("------------------------\n")

def guardar_aprobados(origen="alumnos.txt", destino="aprobados.txt"):
    lineas = leer_alumnos(origen)
    aprobados = []
    
    for linea in lineas:
        partes = [p.strip() for p in linea.split(";")]
        if len(partes) == 4:
            try:
                nota = float(partes[3])
                if nota >= 6:
                    aprobados.append(linea)
            except ValueError:
                continue

    try:
        with open(destino, "w", encoding="utf-8") as f:
            for alumno in aprobados:
                f.write(alumno + "\n")
        print(f"\n--- ARCHIVO {destino} GENERADO ---")
        if not aprobados:
            print("No hay alumnos aprobados.")
        for alumno in aprobados:
            partes = [p.strip() for p in alumno.split(";")]
            print(f"{partes[0]} {partes[1]} - Legajo: {partes[2]} - Nota: {partes[3]}")
        print("----------------------------------\n")
    except Exception as e:
        print(f"Error al generar el archivo de aprobados: {e}")

def menu():
    leer_alumnos("alumnos.txt")
    while True:
        print("1. Ver alumnos")
        print("2. Agregar alumno")
        print("3. Generar y mostrar archivo de aprobados")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            ver_alumnos()
        elif opcion == "2":
            agregar_alumno()
        elif opcion == "3":
            guardar_aprobados()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()