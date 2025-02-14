'''
EJERCICIO 13: VALOR MÁXIMO
En una sola instrucción (de una vez) pide al usuario
que introduzca varios números.
La respuesta del programa será el valor máximo de todos ellos

Por ejemplo, si escribe
2, 5, 3
La respuesta debe ser:
"El valor máximo es 5" 
'''

# SOLUCION

import os
os.system ("cls")

# Pedimos al usuario un conjunto de números
numeros= input("Introduzca los números que desee, separados por una coma --> ")

# Eliminamos los espacios
numeros=numeros.replace(" ","")

# Creamos una lista con los números
lista_numeros= numeros.split(",")
# print(lista_numeros)

# Creamos una lista , inicialmente vacía, que almacenará los números en forma creciente.
lista_ordenada=[]

# Iteramos sobre los elementos de la lista original.
for element in lista_numeros:

    # Si lista_ordenada tiene al menos un elemento
    if lista_ordenada:

        for i in range(len(lista_ordenada)):

            # ordenamos de manera creciente
            if float(element) < float(lista_ordenada[i]):
                lista_ordenada.insert(i,element)   
                # print(34,lista)
                break  
            
        else: # el valor máximo tomará la última posición de la lista
            lista_ordenada.append(element)
            # print(38,lista)

    # Si lista_ordenada aún no tiene elementos                 
    else:
        lista_ordenada.append(element) # agregamos el primer número a lista_ordenada
        # print(42,lista)
    
# print(43,lista)

print(f"El valor máximo es {lista_ordenada[-1]}.")