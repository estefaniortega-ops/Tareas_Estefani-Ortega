"""Programa que calcula el factorial de un número
Autor: Estefani Ortega
Fecha: 25 de octubre de 2026
Descripción: Calcula el factorial de un numero ingresado"""
 

número = int(input("Escribe un número para sacar su factorial: "))
factorial = 1
if número!=0:
    for i in range(1, número + 1):
        factorial = factorial * i
print(f"El factorial es: ", factorial)
