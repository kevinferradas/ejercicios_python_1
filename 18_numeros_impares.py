'''
EJERCICIO 18: NÚMEROS IMPARES
Pídele al usuario que introduzca una serie de números,
comprendidos entre 1 y 20.
El programa debe mostrar los números impares introducidos
o un mensaje indicando que no hay ninguno.

Por ejemplo, si escribe:
2, 5, 3, 6, 9
La respuesta debe ser:
5, 3, 9
'''

import os
os.system ("cls")



# try:

#     #Pedimos al usuario una lista de números. 
#     numeros = input (f""" Escribe una serie de números.
#     >>> """).replace(" ", "").split(",")

    

#     # Definimos una variabla "bandera", que toma inicialmente el valor True.
#     bandera=True

#     # Intentamos hacer el casting int(str) de los elementos de la lista.
    
#     for i, numero in enumerate(numeros) :

#         # Verificamos que los elementos sean números entre 1 y 20.
#         if 1 < int(numero) < 20:
#             numeros [i] =int (numero)
            
        
#         # La variable bandera cambia de valor.
#         else:
#             print(" Los números deben ser enteros y estar contenidos entre 1 y 20.")
#             bandera = False 
#             break

     
#     # En caso las entradas sea numéricos y estén entre 1 y 20
#     # el siguiente código se ejecutará.
#     if bandera:
        
#         # Creamos una lista, inicialmente vacía
#         # que luego se completará con los impares de la lista 
#         # de números ingresada por el usuario
#         impares = []   

#         for numero in numeros:

#             # El residuo de divir un impar con 2 es diferente de cero.
#             if numero % 2 != 0 :
#                 impares.append(str(numero))
        
        
#         # Si la lista de impares tiene al menos un elementos (impares = True)
#         # se ejecutará el siguiente código
#         if impares:
#             print(", ".join(impares))
        
#         # Si la lista de impares sigue vacía (impares = False) es porque no hay impares.
#         else:
#             print("No hay ningún número impar")

#     # En caso una entrada sea no numérica, o flotante
#     # el programa mostrará el siguiente mensaje.   
# except ValueError:
#     print("Debes insertar los números \nde manera numérica ")


try:

    #Pedimos al usuario una lista de números. 
    numeros = input (f""" Escribe una serie de números.
>>> """).replace(" ", "").split(",")


    # Intentamos hacer el casting int(str) de los elementos de la lista.
    
    for i, numero in enumerate(numeros) :

        numeros [i] =int (numero)
        
        
# En caso una entrada sea no numérica, o flotante
# el programa mostrará el siguiente mensaje   
except ValueError:
    print("Debes insertar los números \nde manera numérica ")

# En caso las entradas sea numéricos y estén entre 1 y 20, el siguiente código se ejecutará.    
else:
      
    # Creamos una lista, inicialmente vacía que luego se completará con los impares de la lista 
    # de números ingresada por el usuario
    impares = []
    for numero in numeros:
        if 0 < numero < 20:

            # El residuo de divir un impar con 2 es diferente de cero.
            if numero % 2 != 0 :
                impares.append(str(numero))
        
        else:
            print("Los números deben estar entre 0 y 20.")
            break
        
            
    # Si la lista de impares tiene al menos un elementos (impares = True) se ejecutará el siguiente código
    if impares:
        print(", ".join(impares))
            
    # Si la lista de impares sigue vacía (impares = False) es porque no hay impares.
    else:
        print("No hay ningún número impar")
        