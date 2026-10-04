"""Programa: Calculo del salario neto de un empleado
Autor: Estefani Ortega
Fecha: 3 de octubre 2026
Descripción: Este programa solicita el sueldo bruto de un empleado
y da como resultado el sueldo neto    
    """
#importaciones no necesarias

def calcular_impuesto (impuesto):
    return sueldo * (impuesto / 100)

def deducciones (deducciones):
    return sueldo - deducciones

def sueldo_neto (sueldo):
    return sueldo - impuesto - deducciones


if __name__ == "__main__":
    print ("Calcula tu sueldo neto")
    
#Entrada
sueldo = float(input("Ingresa tu sueldo: "))
impuesto = float(input("Ingresa el porcentaje de impuestos descontados, por ejemplo, 15: "))
deducciones = float(input("Ingresa el porcentaje de deducciones adicionales, por ejemplo, 1000: "))

#Proceso
resultado = sueldo_neto (sueldo)

#Salida

print(f"Tu suelo neto es: {resultado}")