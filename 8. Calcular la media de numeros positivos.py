"""Programa calcular la media de números positivos
Autor: Estefani Ortega
Descripción: Solicitar ingresar números positivos uno por uno y se finaliza
cuando el usuario agrega numero negativo, se muestra la media de
los números positivos"""

suma = 0
contador = 0

while True:
  numero = float(input("Ingresa los números positivos de los cuales quieras saber la media o ingresa número negativo para salir: "))
  
  if numero < 0:
    break

  suma += numero
  contador += 1

if contador > 0:
  media = suma / contador
  print(f"La media de los números positivos ingresados es: {media}")
else:
  print("No se ingresaron números positivos.")