""" Programa contador de dígitos
Autor: Estefani Ortega
Fecha: 25 octubre 2026
Descripción: Solicita al usuario un número entero y determine cuántos dígitos tiene
"""


número = int(input("Ingresa un número entero: "))
i = 0

while número > 0:
    número = número // 10
    i += 1
    
print(f"Ese número tiene {i} dígitos")
