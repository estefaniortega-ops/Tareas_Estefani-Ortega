""" Programa Imprimir números divisibles por 3 y 5
Autor: Estefani Ortega
Fecha 25 octubre 2026
Descripción: programa que imprima todos los números entre 1 y 100 que sean 
divisibles tanto por 3 como por 5.
"""

resultado = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
