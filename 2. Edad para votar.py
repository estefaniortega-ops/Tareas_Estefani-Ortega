""" Programa para saber si alguien tiene edad para votar.
Autor: Estefani Ortega
Fecha: 24 de octubre 2026
Descripcción: programa para determinar si 
una persona es elegible para votar. 
La edad mínima para votar es de 18 años"""

#importaciones no necesarias

edad = int(input("Escribe tu edad: "))

if edad >= 18:
    print(f"Tienes edad para votar ")
else:
    print(f"No tienes la edad para votar ")