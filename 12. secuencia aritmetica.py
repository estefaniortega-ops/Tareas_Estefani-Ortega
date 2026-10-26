""" Programa generador de una secuencia aritmética
Autor: Estefani Ortega
FEcha: 25 octubre 2026
Descripción:Escribe un programa que genere una secuencia aritmética hasta un número 
máximo proporcionado por el usuario.
"""

primer_numero = int(input("Introduce el primer número de la secuencia: "))
diferencia = int(input("Introduce la diferencia entre los números: "))
numero_maximo = int(input("Introduce el número máximo que es 20: "))

termino_actual = primer_numero

print("\nSecuencia aritmética generada:")

while True:
    print(termino_actual, end=" ")
    termino_actual += diferencia
    
    if termino_actual > numero_maximo:
        break

print() 