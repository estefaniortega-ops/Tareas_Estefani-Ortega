""" Vocales y consonante
Autor: Estefani Ortega
Fecha 25 octubre 2026
Descripción: Se solicita  ingresar letras e indicar vocales o consonantes.
El programa deberá terminar cuando el usuario ingrese un espacio
"""
   
while True:
    entrada = input("Ingresa una letra: ")
    
    if entrada == " ":
        print("Programa terminado.")
        break
    
    if entrada in "aeiouáéíóúü":
        print(f"'{entrada}' es una VOCAL.")
    else:
        print(f"'{entrada}' es una CONSONANTE.")
    