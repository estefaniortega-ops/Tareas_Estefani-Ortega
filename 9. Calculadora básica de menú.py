""" Programa calculadora básica de menu
Autor: Estefani Ortega
Fecha: 25 octubre 2026
Descripción: calculadora básica con las operaciones de suma, resta, multiplicación y dividsión, 
Después de realizar una operación, se pregunta si se quiere salir
"""

while True:
    operación = int(input("Elige la operación del 1. suma, 2. resta, 3. multipliación, 4. división, 5. salir:"))
            
    if operación == 1:
        print("suma")
    elif operación == 2: 
        print("resta")
    elif operación == 3:
        print("multiplicación")
    elif operación == 4:
        print("división")
    elif operación == 5:
        print("Programa terminado")
        break