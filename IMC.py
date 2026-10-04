"""Programa: Calcular el IMC (Índice de Masa Corporal)
    Autor: Estefani Ortega
    Fecha: 3 de octubre de 2026
    Descripción: Se solicitan el peso y altura, se calcula el IMC
    se toma como referencia la clasificación de la OMS
    """
#Importaciones no necesarias

#Constantes
CLASIFICACION_IMC = [
    (18.5,"Bajo peso"),
    (25.0,"Normal"),
    (30.0,"Sobrepeso"),
    (float("inf"), "Obesidad")
    ]

def calcular_imc(peso,altura):
    return peso / (altura ** 2)

def clasificación_imc(imc):
  for limite, clasificacion in CLASIFICACION_IMC:
        if imc < limite:
            return clasificacion

#Bloque final
if __name__ == "__main__":
    print("=== Calcula tu  IMC=== ")

#Entrada
peso = float(input("Ingresa tu peso en kilogramos, por ejemplo, 65: "))
altura = float(input("Ingresa tu altura en metros, por ejemplo, 1.60:  "))

#Proceso
imc = calcular_imc(peso,altura)
clasificación = clasificación_imc(imc)
#Salida
print(f"Tu IMC es: {imc}")
print(f"Tu clasificación es: {clasificación}")