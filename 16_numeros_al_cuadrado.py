'''
EJERCICIO 16: NÚMEROS AL CUADRADO
Pídele al usuario que introduzca una serie de números,
comprendidos entre 1 y 20.
El programa debe mostrar el cuadrado de cada uno de los números.

Por ejemplo, si escribe:
2, 5, 3
La respuesta debe ser:
4, 25, 9
'''
# SOLUCION

import os
os.system ("cls")



try:

    
    # Pedimos al usuario un conjunto de números.
    # Eliminamos los espacios con .replace.
    # Creamos una lista con los números con split()
    lista_numeros= input("Introduzca los números que desee, separados por una coma --> ").replace(" ","").split(",")


    # las "banderas"(centinelas) se refieren a variables booleanas  que nos permite saber si cierta parte del 
    # código se ha ejecutado o no, esto lo hace cambiando entre dos posibles valores
        
    bandera = True

    # iteramos sobre los elementos de la lista    
    for indice, numero in enumerate(lista_numeros):

        # Verificamos si el número es un entero entre 1 y 20
        if int(numero) not in range(2,20):
            print ("Los números deben estar contenidos entre 1 y 20.")
            bandera= False
            break # basta que un caracter no esté en el rango indicado
                  # para parar el programa.

    
        # casting: str --> int
        else:
            numero=int(numero) # casting: str --> int
            lista_numeros[indice]=numero
    
    # Si la variable bandera sigue siendo positiva, se ejecutará el resto del código.
    if bandera:
        

        lista_numeros_cuad=[]

        # Creamos una lista con los cuadrados de los números.
        for  numero in lista_numeros:
            numero_cuad = numero**2
            lista_numeros_cuad.append(str(numero_cuad))

        # Presentamos la lista de cuadrados separados por una coma.
        print(", ".join(lista_numeros_cuad))
        
            

except ValueError:
    print("Debe introducir valores numéricos, separados por coma")