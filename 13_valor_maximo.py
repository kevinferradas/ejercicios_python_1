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

numeros= input("Introduzca los números que desee separados por una coma --> ")
numeros=numeros.replace(" ","")
lista_numeros= numeros.split(",")

lista=[]
for element in lista_numeros:
    if lista:
        for i in range(len(lista)):
            if element < lista[i]:
                lista.append(element)
                print(28,lista)
                numero_menor=lista[i+1]
                numero_mayor=lista[i]
                lista[i]=numero_menor
                lista[i+1]=numero_mayor
                print(33,lista)
                break  
            else:
                lista.append(element)
                print(37,lista)
                break     
    else:
        lista.append(element)
        print(41,lista)
    
print(43,lista)