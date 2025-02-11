"""
EJERCICIO 2 : ÁREA DE UN TRIÁNGULO
Haz un programa que pida al usuario dos números, 
indicando que son la base y la altura de un triángulo
La respuesta del programa será:
"El área de un triángulo de base X y altura Y es Z" (los valores que sean)
"""

import os
os.system ("cls")

# base y altura del triángulo
base = int(input("Inserta la medida de la base -> "))
altura =int(input("Inserta la medida de la altura -> "))

# área del triángulo
area= 0.5*base*altura
print(f"El área de un triángulo de base {base} y {altura}  es {area} unidades cuadradas.")