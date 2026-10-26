""" Programa para calcular el precio final de un producto
Autor: Estefani Ortega
Fecha: 24 octubre 2026
Descripción: Precio final de un producto aplicando el descuento correspondiente según el precio original:
Precio ≤ 100: Sin descuento
Precio > 100 y ≤ 200: 10 por ciento de descuento
Precio > 200 y ≤ 500: 20 por ciento de descuento
Precio > 500: 25 por ciento de descuento
"""

#importaciones no necesarias
precio = float(input("Ingresa el precio del producto: "))
descuento1 = 10
descuento2 = 20
descuento3 = 25

precio1 = (precio * descuento1) / 100
precio2 = (precio * descuento2) / 100
precio3 = (precio * descuento3) / 100

if precio <= 100:
    print("No tienes descuento")
elif precio >= 100 and 200:
    print(precio - precio1)
elif precio >= 200 and 500:
    print (precio - precio2)
elif precio > 500:
   print(precio - precio3)
else: 
    print("No es válida la cantidad")

