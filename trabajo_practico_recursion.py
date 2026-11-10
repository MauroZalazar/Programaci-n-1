class Archivo:
    def __init__(self, nombre: str, tamano_bytes: int):
        self.nombre = nombre
        self.tamano_bytes = tamano_bytes

class Directorio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.archivos = []
        self.subdirectorios = []

def calcular_tamano_total(directorio: Directorio) -> int:
    total = sum(archivo.tamano_bytes for archivo in directorio.archivos)
    for sub in directorio.subdirectorios:
        total += calcular_tamano_total(sub)
    return total

def buscar_por_extension(directorio: Directorio, extension: str, ruta_actual: str = "") -> list[str]:
    actual = f"{ruta_actual}/{directorio.nombre}" if ruta_actual else directorio.nombre
    resultados = []
    
    for archivo in directorio.archivos:
        if archivo.nombre.endswith(extension):
            resultados.append(f"{actual}/{archivo.nombre}")
            
    for sub in directorio.subdirectorios:
        resultados.extend(buscar_por_extension(sub, extension, actual))
        
    return resultados

def limpiar_archivos_vacios(directorio: Directorio) -> int:
    eliminados = 0
    archivos_validos = []
    
    for archivo in directorio.archivos:
        if archivo.tamano_bytes == 0:
            eliminados += 1
        else:
            archivos_validos.append(archivo)
            
    directorio.archivos = archivos_validos
    
    for sub in directorio.subdirectorios:
        eliminados += limpiar_archivos_vacios(sub)
        
    return eliminados