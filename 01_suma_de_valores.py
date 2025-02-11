"""
EJERCICIO 1 : SUMA DE VALORES
Haz un programa que pida al usuario dos números para sumarlos.
La respuesta del programa será:
"La suma de los dos números es XX" (el valor que sea)
"""

import os
os.system ("cls")

# Pedimos al usuario insertar dos números
num_1 = int(input ("Inserta un número -> "))
num_2 = int(input("Inserta otro número"))

# Imprimimos la suma.
print(f"La suma de los dos números es {num_1 + num_2}. ")