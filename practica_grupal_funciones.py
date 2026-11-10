class ValidadorFinanciero:
    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:
        return cuit.isdigit() and len(cuit) == 11

    @staticmethod
    def convertir_moneda(monto: float, tasa_cambio: float, comision: float = 0.02) -> float:
        monto_convertido = monto * tasa_cambio
        return monto_convertido * (1 - comision)


class Notificador:
    def enviar_recibo(self, cliente: str, total: float) -> None:
        print(f"Recibo de pago para {cliente}. Total abonado: {total}")


class ProcesadorPagos:
    def __init__(self, notificador: Notificador = None):
        self.notificador = notificador if notificador else Notificador()

    def procesar_transaccion(self, cliente: str, items: list[dict], descuento_cupon: float = 0.0) -> float:
        subtotal = sum(item["precio"] for item in items)
        total = subtotal - descuento_cupon
        if total < 0:
            total = 0.0
        self.notificador.enviar_recibo(cliente, total)
        return total


class CalculadoraFitness:
    @staticmethod
    def calcular_imc(peso_kg: float, altura_m: float) -> float:
        if altura_m <= 0:
            return 0.0
        return peso_kg / (altura_m ** 2)

    @staticmethod
    def clasificar_nivel(imc: float) -> str:
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25.0:
            return "Normal"
        else:
            return "Sobrepeso"


class Atleta:
    def __init__(self, nombre: str, peso: float, altura: float):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def obtener_reporte(self, incluir_recomendacion: bool = False, **metricas_extra) -> str:
        imc = CalculadoraFitness.calcular_imc(self.peso, self.altura)
        nivel = CalculadoraFitness.clasificar_nivel(imc)
        
        reporte = f"Atleta: {self.nombre}\nPeso: {self.peso} kg\nAltura: {self.altura} m\nIMC: {imc:.2f}\nNivel: {nivel}"
        
        if metricas_extra:
            reporte += "\nMétricas Extra:"
            for clave, valor in metricas_extra.items():
                reporte += f"\n- {clave.upper()}: {valor}"
                
        if incluir_recomendacion:
            if nivel == "Bajo peso":
                rec = "Aumentar ingesta calórica y entrenamiento de fuerza."
            elif nivel == "Normal":
                rec = "Mantener plan de entrenamiento actual y nutrición equilibrada."
            else:
                rec = "Ajustar déficit calórico y sumar actividad aeróbica."
            reporte += f"\nRecomendación: {rec}"
            
        return reporte


def calcular_factura_final(monto_base: float, impuesto: float = 21.0, descuento: float = 0.0, envio_prioritario: float | None = None) -> float:
    monto_descontado = monto_base * (1 - descuento / 100)
    subtotal = monto_descontado * (1 + impuesto / 100)
    if envio_prioritario is not None:
        subtotal += envio_prioritario
    return round(subtotal, 2)


def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
    lineas = [f"MODULO: {modulo.upper()}"]
    for i, mensaje in enumerate(mensajes, start=1):
        lineas.append(f"[{i}] {mensaje}")
    for clave, valor in metadatos.items():
        lineas.append(f"{clave.upper()}: {valor}")
    return "\n".join(lineas)