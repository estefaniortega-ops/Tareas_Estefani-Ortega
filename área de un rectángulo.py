"""Programa para calcular el área de un rectángulo
    Autor: Estefani Ortega
    Fecha: 3 de octubre de 2026
    Descripción: Este programa solicita la base y la
    altura de un rectángulo para conocer su área
    """
#Importaciones no necesarias

#saber el área de un rectángulo cuando el usuario proporciona los datos
def calcular_área (a,b):
    return (a * b)

#Bloque principal
if __name__ == "__main__":
    print ("=== Calcular el área de un rectágulo")
    
#Entrada de datos
a = float(input("Ingresa la base del rectángulo: "))
b = float(input("Ingresa la altura del rectángulo: "))

#Proceso
resultado = calcular_área (a,b)
#Salida
print(f"El área del rectángulo es: {resultado}")
