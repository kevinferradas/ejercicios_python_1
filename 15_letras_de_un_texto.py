'''
EJERCICIO 15: LETRAS DE UN TEXTO
Haz un programa que pida al usuario un texto.
El programa debe mostrar las letras que aparecen en ese texto
ordenadas de forma alfabética, pero solo una vez por cada letra,
y siempre en minúsculas.

Por ejemplo, si escribe: "Hoy es domingo"
La respuesta debe ser: "deghimnoy"
'''

import os
os.system ("cls")

# Pedimos al usuario un texto.
texto= input("Introduzca un texto --> ").lower()

#Eliminamos los espacios
texto=texto.replace(" ","")
print(texto)

# La lista de letras almacenará las letras del texto, y en caso de repetición, solo almacenará una.
lista_letras=[]
for letra in texto:
    if letra not in lista_letras:
        lista_letras.append(letra)

print(lista_letras)

# Creamos una lista , inicialmente vacía, que almacenará las letras en orden alfabético.
lista_ordenada=[]

# Iteramos sobre los elementos de la lista original.
for element in lista_letras:

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
