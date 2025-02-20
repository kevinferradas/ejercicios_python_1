"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 1

Un número primo es aquel que sólo es divisible por sí mismo o uno.

Pediremos al usuario un número entero.
Si escribe algo que no sea un número entero la aplicación debe responder: 
    "Has de introducir un número entero".
Daremos hasta tres oportunidades para que nos facilite un dato correcto.
Pero si pasadas esas tres oportunidades sigue sin escribir un entero 
la aplicación finalizará mostrando este mensaje:
    "No has podido introducir un número entero en tres oportunidades
    Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.
    ".
Si escribe un número entero puede pasar que
-- sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X es primo".
-- no sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X no es primo".

. 
"""
# Alumno: Kevin Ferradas
######## SOLUCIÓN ########

import os
os.system ("cls")

'''
-Todos los números son divisibles por 1 y por ellos mismos.

- Para comprobar que el número es primo, intentaremos descubrir 
si es divisible por algún número en el intervalo [2,numero]. Para estos usaremos
el operador módulo (%).

-Por otro lado, el máximo divisor posible de un número,dejando de lado el mismo número, es su mitad.
Ej: 20: 1,2,4,5,10,20. El máximo divisor de 20, después del mismo 20, es el 10.
Luego, solo hará falta descubrir si es divisible por algún número en el intervalo [2,numero/2]
'''




intentos=1 

# El usuario tiene máximo 3 intentos. 
# El código se ejecutará mientras no se haya intentado más de 3 veces
while intentos <= 3:  

    #intentamos ejecutar el código
    try: 
        
        #Pedimos al usuario un número entero
        numero= int(input("\nEscribe un número entero -> ")) 
        
        # Verificamos si el número es divisible por algún número distinto al 1 y a él mismo.
        for x in range(2,(numero//2) +1): 

            # Si el residuo (módulo) de divir el número con otro "x" es cero
            # significa que es divisible por dicho número
            # Luego, el número no es primo.
            if numero % x ==0: 
                print(f"\nEl número {numero} no es primo.") 

                # Basta que el número sea divisible por un solo número distinto de 1 o él mismo
                # para que no sea primo.
                break # detenemos el bucle for antes de que recorra todos los elementos.

        # Si el número no es divisble por ningún número en el rango indicado, 
        # la única opción es que se trate de un número primo
        else: 
            print(f"\nEl número {numero} es primo") 
        # si el número resulta primo, detenemos el bucle while.
        break 

    # Si el input no es un número entero (Value error), aparece un mensaje de error.
    except ValueError: 

        # Tras cada excepción, el valor de intentos aumentará una unidad.
        intentos +=1
        
        # Mostramos mensaje al usuario
        if intentos <=3:
            print("\nHas de introducir un número entero")
            print(f"\nTe quedan {4- intentos } intentos.")

                
else: # Pasados los 3 intentos,la aplicación finaliza mostrando un mensaje.
    print("\nNo has podido introducir un número entero en tres oportunidades \nPuedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.\n")




    
    

        



        


    