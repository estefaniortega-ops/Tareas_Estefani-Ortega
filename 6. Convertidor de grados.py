""" Programa que determina para convertir temperatura
Autor: Estefani Ortega
Fecha: 24 de octubre 2026
Descripción: Convertir la temperatura ingresada en grados Celsius a Fahrenheit o Kelvin, 
según la elección del usuario.
"""
#importaciones no necesarias

Temperatura = float(input("Ingresa la temperatura en grados Celsuis: "))

Farenheit = (Temperatura * 9/5) + 32
Kelvin = (Temperatura + 273.15)

while Temperatura <= 2:
    print("1. Farenheit")
    print("2. Kelvin")
    
Temperatura2 = float(input("Selecciona una opción 1 Farenheit o 2 Kelvin: "))
match Temperatura2:
        case 1:
            print("La temperatura en Farenheit es: ", Farenheit) 
        case 2:
            print("La temperarura en Kelvin es: ", Kelvin)
        case _:
            print("no válido")
            