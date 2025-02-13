'''
EJERCICIO 8: CONVERSIÓN DE MONEDAS
Haz un programa que pida al usuario la cantidad de euros que quiere convertir a dólares
La respuesta del programa será:
"X euros equivalen a Y dólares" (los valores que sean)
Formúla de conversión : 1 euro = 1.18 dólares
'''

import os
os.system ("cls")

#EQUIVALENCIA
euro_a_dolar=1.18
try:
    euros = float(input("Ingrese la cantidad de euros que desee convertir a dólares -> ")) 
    print(f"{euros} euros equivalen a {euros*euro_a_dolar} dólares.")

except ValueError:
    print("Debe ingresar un número.")
