""" Programa que asigna una letra a una calificación
Autor: Estefani Ortega
Descripción: Escribe un programa que reciba una calificación numérica y
asigne una letra de acuerdo con los siguientes rangos: 90 a 100: A
80 a 89: B
70 a 79: C
60 a 69: D
Menos de 60: F
"""

#importaciones no necesarias

calificación = int(input("Ingresa tu calificación en un rango del 0 al 100: "))
        
if calificación > 90 and 100:
    print(f"A")
elif calificación > 80 and 89:
    print(f"B")
elif calificación > 70 and 79:
    print(f"C")
elif calificación > 60 and 69:
    print(f"D")
elif calificación < 60:
    print(f"F")
else: 
    print(f"Calificación no válida")
