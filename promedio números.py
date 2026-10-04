"""
   Programa para calcular el promedio de tres números
   Autor: Estefani Ortega
   Fecha: 2 de octubre 2026
   Descripción: Este programa solicita tres números
   para sacar un promedio"""
   
   #importaciones no necesarias
   #Saber el área de un rectángulo cuando el usuario establece los datos
def calcular_promedio (a,b,c,):
    #calcular el promedio de las variables
    return (a + b + c) / 3

#bloque principal
if __name__ == "__main__":
    print ("=== Calculador de promedio ===")

#Entrada de datos
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

#Proceso
resultado = calcular_promedio (a,b,c)

#Salida
print (f"El promedio de los tres número es: {resultado}")

