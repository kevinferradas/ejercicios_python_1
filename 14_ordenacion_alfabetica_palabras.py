'''
EJERCICIO 14: ORDENACIÓN ALFABÉTICA DE PALABRAS
Haz un programa que pida al usuario un texto.
El programa debe ordenar las palabras del texto de forma alfabética.

Por ejemplo, si escribe: "hoy es domingo"
La respuesta debe ser: "domingo es hoy"
'''

import os
os.system ("cls")

texto = input("Escriba un texto -> ")
lista_ordenada=[]
lista_palabras = texto.split(None)
print(lista_palabras)

for palabra in lista_palabras:
    if lista_ordenada:
        for item in lista_ordenada: 
            if palabra > item:
                lista_ordenada.append(palabra)
                break
                
            else:
                lista_ordenada.append(palabra)
                lista_ordenada_0 = lista_ordenada[0]
                lista_ordenada_1 = lista_ordenada[-1]
                lista_ordenada[0]= lista_ordenada_1
                lista_ordenada[-1]= lista_ordenada_0
                break
        
    else:
        lista_ordenada.append(palabra)

print(lista_ordenada)
