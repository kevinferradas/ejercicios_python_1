'''
EJERCICIO 7: POSITIVO, NEGATIVO O CERO
Haz un programa que pida al usuario un número y diga si es positivo, 
negativo o cero
'''
import os
os.system ("cls")

try:
    numero = float(input("Escriba un número -> "))
    
    if numero<0:
        print(f"El número {numero} es negativo.")
    elif numero>0:
        print(f"El número {numero} es positivo.")
    else:
        print("El número es cero")

except ValueError:
    print("Debe ingresar un número")