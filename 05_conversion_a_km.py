"""
EJERCICIO 5 : CONVERSIÓN A KM
Haz un programa que haga lo opuesto a lo anterior,
convertir millas a kilómetros
"""
import os
os.system ("cls")

try:
    distancia=float(input("Escriba la distancia (en millas) que desee convertir a kilómetros --> "))

    #equivalencia km en millas
    km_a_milla= 0.621371
    # equivalencia millas en km
    # nª kilometros= nº millas x( 1/0.621371) km

    print(f"{distancia} millas equivalen a {round(distancia/0.621371,2)} kilómetros.")
except ValueError:
    print("Debes escbrir un número.")