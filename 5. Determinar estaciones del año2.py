""" Programa que determina la estación del año
a partir del mes que se escribe
Autor: Estefani Ortega
Descripción: Se solicita el mes al usuario y da como resultado
la estación del año
"""
#importaciones no necesarias
estacion = int (input("Ingresa un número del 1 al 12 para saber en que estación del año estás: "))
        
match estacion:
        case 1:
            print("invierno")
        case 2:
            print("invierno")
        case 3:
            print("primavera")
        case 4:
            print("primavera")
        case 5:
            print("primavera")
        case 6:
            print("verano")
        case 7:
            print("verano")
        case 8: 
            print("verano")
        case 9:
            print("otoño")
        case 10:
             print("otoño")
        case 11:
            print("otoño")
        case 12: 
            print("invierno")
        case _:
            print("no es un número válido")

