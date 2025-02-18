'''
EJERCICIO 17: SEGUNDO NÚMERO MAYOR
Pídele al usuario que introduzca una serie de números,
comprendidos entre 1 y 20.
El programa debe mostrar el segundo número mayor.

Por ejemplo, si escribe:
2, 5, 3, 6, 9
La respuesta debe ser:
"El segundo número mayor es 6"
'''

import os
os.system ("cls")

# Pedimos al usuario que inserte una lista de números
lista_numeros=[]

# El usuario insertará la cantidad de números que desee
# Para parar, deberá presionar s
while True:
    numero=input(f"""Introduce varios números , uno a la vez
(presiona de insertar un número, haz enter)
>>> """).replace(" ","").lower()
    
    if numero== "s":
        break
    else:
        lista_numeros.append(numero)



try:

    # Los elementos de la lista_números son str.
    # Intentamos hacer el casting : float(str)
    for indice, valor in enumerate(lista_numeros):
        lista_numeros[indice]=float(valor)

    print(lista_numeros)

    # Creamos una lista inicialmente vacía
    # Luego, contenerá los números ordenados ascendentemente. 
    lista_ordenada=[]

    for numero in lista_numeros:

        # Verificamos que las entradas sean números entre 1 y 20.
        if 1<numero<20:


            # A partir del segundo elemento (lista_ordenada = True),
            # se ejecutará esta acción
            if lista_ordenada:
                
                # Ordenamos los números de menor a mayor.
                for i in range(len(lista_ordenada)):

                    if numero < lista_ordenada[i]:
                        
                        lista_ordenada.insert(i,numero)
                        break
                else:
                    lista_ordenada.append(numero)
                
            # Como la la lista está inicialmente vacía (False)
            # entonces primero se ejecutará esta acción.    
            else:
                lista_ordenada.append(numero)
        else:
            print("Los números deben estar entre 1 y 20")
            break
    
    # Por la manera en que hemos ordenado
    # El segundo número mayor de la lista es el penúltimo elemento
    # Es decir, lista_ordenada [-2]
    print(f"El segundo número mayor es {lista_ordenada[-2]}.")
    
    print(lista_ordenada)

# Si alguna de las entradas del usuario es no numérico
# El programa mostrará este mensaje.
except:
    print("Debe introducir valores numéricos  ")