"""Contador de números impares 
Autor: Estefani Ortega
Fecha: 25 octubre 2026
Descripción: Solicita al usuario un número entero positivo y muestra todos los 
números impares desde 1 hasta ese número."""


número = int(input("Ingrese un número entero positivo: "))
n = 1
contador = 0

while True:
    if número % 2 != 0:
        print(número)
    if número < n:
        break