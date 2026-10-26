""" Programa para contar letras
Autor: Estefani Ortega
Fecha: 25 de octubre 2026
Descripción: contar letras 'a' en una palabra ingresada por el usuario.
"""

contador = 0
letra = "a"
palabra = str(input("Ingrese una palabra: "))

for letra in palabra:
    if letra in "a":
        contador += 1
print(f"La palabra tiene {contador} letras a")


