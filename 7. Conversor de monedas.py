""" Programa que convierte en pesos mexicano otras monedas
Autor: Estefani Ortega
FEcha:24 octubre 2026
Descripción: convierte una cantidad en pesos mexicanos a diferentes monedas 
utilizando una estructura match-case.
Opciones de conversión:
1. Dólar (USD)
2. Euro (EUR)
3. Bath (THB)
4. Yen (JPY)
5. Won (KRW)
6. Dólar Australiano (AUD)
7. Sol (PEN)
8. Dólar Canadiense (CAD)
9. Bolívar (VES)
10. Peso Argentino (ARS)
"""

#constantes
Dolar = 18 
Euros = 20
Bath = .55
Yen = .12
Won = 0.014
Dólar_australiano = 13.08
Sol = 5.44
Dólar_canadiense = 13.39
Bolívar =  0.0211
Peso_Argentino = 0.012

Conversión = float(input("Ingresa la cantidad en pesos mexicanos (MXN): "))

while Conversión <= 10:
    print("1. Dólar")
    print("2. Euros")
    print("3. Baht")
    print("4. Yen")
    print("5. Won")
    print("6. Dólar_australiano")
    print("7. Sol")
    print("8. Dólar_canadiense")
    print("9. Bolívar")
    print("10. Peso_Argentino")

Conversión2 = int(input("Selecciona una opción (1-10): "))

match Conversión2:
        case 1:
            print("El equivalente en dólar americano es: ", Conversión * Dolar) 
        case 2:
            print("El equivalente en Euros es: ", Conversión * Euros)
        case 3:
            print("El equivalente en Bath es: ", Conversión * Bath)
        case 4:
            print("El equivalente en Yenes es: ", Conversión * Yen)
        case 5:
            print("El equivalente en Wones es: ", Conversión  * Won)
        case 6:
           print("El equivalente en dólar australiano es: ", Conversión * Dólar_australiano)
        case 7:
           print("El equivalente en Soles es: ", Conversión * Sol)
        case 8:
           print("El equivalente en dólar canadiense es: ", Conversión * Dólar_canadiense)
        case 9:
            print("El equivalente en Bolívares es: ", Conversión * Bolívar)
        case 10:
            print("El equivalente en pesos argentinos es: ", Conversión * Peso_Argentino)
        case _:
            print("Opción no válida. Por favor, selecciona un número del 1 al 10.")
