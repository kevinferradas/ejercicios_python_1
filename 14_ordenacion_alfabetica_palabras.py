'''
EJERCICIO 14: ORDENACIÓN ALFABÉTICA DE PALABRAS
Haz un programa que pida al usuario un texto.
El programa debe ordenar las palabras del texto de forma alfabética.

Por ejemplo, si escribe: "hoy es domingo"
La respuesta debe ser: "domingo es hoy"
'''

# SOLUCION

import os
os.system ("cls")

# Pedimos al usuario un texto.
texto= input("Introduzca un texto --> ")

# Eliminamos los espacios y creamos una lista cuyos elementos son las palabras del texto.
lista_palabras=texto.split(None)


# Creamos una lista , inicialmente vacía, que almacenará las palabras en orden alfabético.
lista_ordenada=[]

# Iteramos sobre los elementos de la lista original.
for element in lista_palabras:

    # Si lista ordenada tiene al menos un elemento
    if lista_ordenada:

        for i in range(len(lista_ordenada)):

            # ordenamos de manera creciente
            if element < lista_ordenada[i]:
                lista_ordenada.insert(i,element)   
                # print(34,lista)
                break  
            
        else: # la palabra "mayor", alfabéticamente hablando, toma la última posición
            lista_ordenada.append(element)
            # print(38,lista)

    # Si lista_ordenada aún no tiene elementos                 
    else:
        lista_ordenada.append(element) # agregamos la primera palabra a la lista ordenada.
        # print(42,lista)
    
# print(43,lista)

texto_ordenado = " ".join(lista_ordenada)
print(texto_ordenado)
