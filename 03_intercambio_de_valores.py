"""
EJERCICIO 3 : INTERCAMBIO DE VALORES
Haz un programa que pida al usuario dos valores (de cualquier tipo), 
por ejemplo así:
"Escribe el valor de la primera variable (a) --> "
Supongamos que responde X; lo guardas en la variable a
"Escribe el valor de la segunda variable (b) --> "
Supongamos que responde Y; lo guardas en la variable b
A continuación debes hacer que b tenga el valor de a y a el de b,
es decir, deben intercambiar sus valores
La respuesta del programa será:
"Ahora a vale Y y b vale X" (los valores que sean)
"""

import os
os.system ("cls")

# Pedimos al usuario que asigne un valor a dos variables a y b.
a = input(" Escribe el valor de la primera variable (a) -> " )
b = input (" Escribe el valor de la segunda variable (b) -> " )

# Definimos dos variables que almacenan los valores originales de a y b.
a_b=b
b_a=a

# Reasignamos a las variables a y b el valor del otro.
a=a_b 
b=b_a 


print(f"Ahora a vale {a} y b vale {b}.")
