'''
EJERCICIO 6: CONVERSIÓN A GRADOS CELSIUS
Haz un programa que pida al usuario la temperatura en grados Fahrenheit
La respuesta del programa será:
"X grados Fahrenheit equivalen a Y grados Celsius" (los valores que sean)
Formúla de conversión : Fahrenheit = (Celsius * 9/5) + 32
'''

import os
os.system ("cls")

# equivalencia C a F


try:
    Fahrenheit=float(input("Escriba la temperatura (en F) que desea convertir a grados Celsius --> "))
    Celsius= (5/9) * (Fahrenheit - 32)
    print(f"{Fahrenheit} grados Fahrenheit equivalen a {round(Celsius,3)} grados Celsius. ")
except:
    print("Debe ingresar un número.")