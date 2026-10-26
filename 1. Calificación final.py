"""Programa: Calcular la calificación final de un estudiante
    Autor: Estefani Ortega
    Fecha: 23 de octubre de 2026
    Descripción: Se solicitan tres calificaciones en un 
    rango del 0 al 100 para calcular la calificación final
    """
    
    #Importaciones no necesarias
 
  
parcial = float(input("anota la calificación parcial: "))
proyecto = float(input("Anota la calificación de tu proyecto: "))
examen = float(input("Anota la calificación de tu examen final: "))

calificación1 = parcial * 40 / 100
calificación2 = proyecto * 30 / 100
calificación3 = examen * 30 / 100

promedio = (calificación1 + calificación2 + calificación3)

if promedio <= 100:
    print(f"Tu calificación final es: ", promedio)
else: 
    print(f"Calificación no válida")

    
    
