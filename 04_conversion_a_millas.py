"""
EJERCICIO 4 : CONVERSIÓN A MILLAS
Haz un programa que pida al usuario la distancia a convertir (en km)
Redondea el resultado a dos decimales
La respuesta del programa será:
"X km equivalen a Y millas" (los valores que sean)
Nota: 1 km son 0.621371 millas
"""



try:
    distancia=float(input("Escriba la distancia (en km) que desee convertir a millas --> "))

    #equivalencia en millas
    km_a_milla= 0.621371

    print(f"{distancia} kilómetros equivalen a {round(distancia*km_a_milla,2)} millas.")
except ValueError:
    print("Debes escbrir un número.")