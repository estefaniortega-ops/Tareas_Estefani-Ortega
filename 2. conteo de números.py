"""Programa para contar números
Autor: Estefani Ortega
Descripción: Solicitar una cantidad de número y saber cuantos
son mayores, menores o igual a 0"""

for i  in range(1, 101):
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        print("El número es mayor que 0")
    elif numero < 0:
        print("El número es menor que 0")
    else:
        print("El número es igual a 0")