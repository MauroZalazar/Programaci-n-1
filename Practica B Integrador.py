# 1. Diccionario de alumnos { Legajo: "Apellido y Nombre" }
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

# 2. Lista de materias por defecto (Materia, Nota 1, Nota 2, Nota Final)
# Usamos una lista base que luego clonaremos o reiniciaremos por alumno
materias_base = [
    ["Ciencias", 0.0, 0.0, 0.0],
    ["Historia", 0.0, 0.0, 0.0],
    ["Geografia", 0.0, 0.0, 0.0],
    ["Matematicas", 0.0, 0.0, 0.0],
    ["Fisica", 0.0, 0.0, 0.0]
]

# 3. Lista para notas finales[cite: 1]
notas_finales = []

# 1. Diccionario de alumnos { Legajo: "Apellido y Nombre" }
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

# 2. Lista de materias por defecto (Materia, Nota 1, Nota 2, Nota Final)
materias_base = [
    ["Ciencias", 0.0, 0.0, 0.0],
    ["Historia", 0.0, 0.0, 0.0],
    ["Geografia", 0.0, 0.0, 0.0],
    ["Matematicas", 0.0, 0.0, 0.0],
    ["Fisica", 0.0, 0.0, 0.0]
]

# 3. Lista para notas finales
notas_finales = []

mejor_promedio_general = -1
mejor_alumno = ""

# Iterar el diccionario de alumnos
for legajo, nombre in alumnos.items():
    print(f"\n----------------------------------------")
    print(f"Alumno: {nombre} (Legajo: {legajo})")
    print(f"----------------------------------------")
    
    # Copiamos las materias para este alumno
    materias_alumno = [row[:] for row in materias_base]
    suma_notas_finales = 0
    materia_mas_alta = ""
    nota_mas_alta = -1
    
    # Recorrer la lista de materias y solicitar notas (0 a 10)
    for i in range(len(materias_alumno)):
        materia_nombre = materias_alumno[i][0]
        print(f"\nIngrese las notas para la materia {materia_nombre}")
        
        # Validar Nota 1 (0 a 10)
        while True:
            try:
                n1 = float(input("Nota 1: "))
                if 0 <= n1 <= 10:
                    break
                print("Error: La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
        # Validar Nota 2 (0 a 10)
        while True:
            try:
                n2 = float(input("Nota 2: "))
                if 0 <= n2 <= 10:
                    break
                print("Error: La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
        # Calcular Nota Final de la materia (promedio de las 2)
        n_final = (n1 + n2) / 2
        
        # Asignar a la segunda, tercera y cuarta columna
        materias_alumno[i][1] = n1
        materias_alumno[i][2] = n2
        materias_alumno[i][3] = n_final
        
        print(f"Nota Final {materia_nombre}: {n_final}")
        
        suma_notas_finales += n_final
        
        # Determinar la materia con la calificación más alta
        if n_final > nota_mas_alta:
            nota_mas_alta = n_final
            materia_mas_alta = materia_nombre

    # Mostrar por pantalla la lista materias completa cargada
    print(f"\n--- LISTA DE MATERIAS COMPLETA: {nombre} ---")
    print("Materia      | Nota 1 | Nota 2 | Nota Final")
    print("-" * 42)
    for mat in materias_alumno:
        print(f"{mat[0]:<12} | {mat[1]:<6} | {mat[2]:<6} | {mat[3]:<6}")

    # Mostrar la materia con la calificación más alta para el alumno
    print(f"\nMateria con calificación más alta: {materia_mas_alta} ({nota_mas_alta})")

    # Calcular el promedio general del alumno
    promedio_general = suma_notas_finales / len(materias_alumno)
    
    # Asignar a la lista notas Finales
    notas_finales.append([nombre, promedio_general])
    
    # Determinar cuál de todos los alumnos posee el mejor promedio
    if promedio_general > mejor_promedio_general:
        mejor_promedio_general = promedio_general
        mejor_alumno = nombre

# Resultado final global de todos los alumnos
print("\n========================================")
print(f"MEJOR ALUMNO GENERAL: {mejor_alumno} con un promedio de {mejor_promedio_general}")
print("========================================")