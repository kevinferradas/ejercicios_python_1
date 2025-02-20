"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 3
Un anagrama es un texto o palabra resultante de modificar el orden de otro texto o palabra.
Los textos deberán ir sin tildes (acentos o diéresis)
No se tienen en cuenta mayúsculas ni espacios.

Mostraremos el mensaje: "Anagramas"
Pediremos al usuario un texto/palabra.
Pediremos al usuario un segundo texto/palabra
Responderemos si ambos son anagramas o no.

Por ejemplo:
    "Introduzca el primer texto --> " Pedro
    "Introduzca el segundo texto --> " Poder
    "Son anagramas --> Sí"

Otro ejemplo:
    "Introduzca el primer texto --> " Ramon
    "Introduzca el segundo texto --> " Morir
    "Son anagramas --> No"
 
"""
# Alumno: Kevin Ferradas
######## SOLUCIÓN ########

import os
os.system ("cls")

'''
- La idea es comprobar si dos textos son anagramas.

- El programa primero convierte todos los caracteres a minúsculas y luego
suprime todos los espacios, convirtiendo por separado cada texto a una sola cadena.

- Luego, usando el bucle for y el método .append() , creamos dos listas, donde cada una almacena
las letras de los correspondientes textos.

-El primer requisito es que ambas listas tengan la misma cantidad de elementos.

-El segundo requisito es que todos los elementos de una lista estén también en el otro, teniendo cuidado
 en los casos donde haya repeticiones de letras.
'''


print("Anagramas")

# Pedimos al usuario un texto o palabra.
# Los textos deberán ir sin tildes (acentos o diéresis)
texto_palabra_1=input("Escribe un texto o palabra -> ")
texto_palabra_2=input("Escribe un segundo texto o palabra -> ")

# No se tienen en cuenta mayúsculas
texto_palabra_1=texto_palabra_1.lower()
texto_palabra_2=texto_palabra_2.lower()

# No se tienen en cuenta espacios
texto_palabra_1=texto_palabra_1.replace(" ","")
texto_palabra_2=texto_palabra_2.replace(" ","")


letras_1=[]
for letras in texto_palabra_1:

    #Creamos una lista con las letras del texto 1.
    letras_1.append(letras)
# print(letras_1)
    
letras_2=[]
for letras in texto_palabra_2:
    #Creamos una lista con las letras del texto 1.
    letras_2.append(letras)
# print(letras_2)

# Para que sean anagramas, la cantidad de letras ha de ser la misma.
if len(letras_1) == len(letras_2):
                    
    for i in range(len(letras_1)):

        # Si alguna letra del texto 1 no está contenida en el texto 2
        # automáticamente las palabras no son anagramas
        if letras_1[i] not in letras_2:
            print(" \nSon anagramas --> No")
            break # detenemos el bucle for antes de que recorra todos los elementos.

        # texto_1= pedroo; texto_2= ppoder
        # No son anagramas, a pesar de contener los mismos caracteres
        # Para que dos palabras sean anagramas, cada elemento del texto 1
        # debe relacionarse con un único elemento del texto 2
        else:
            # removemos la primera aparición de la letra, en la lista 2.
            # Así, aseguramos que cada elemento del texto 1 
            # esté relacionado con un único elemento del texto 2
            letras_2.remove(letras_1[i]) 
            

    # Si todas las letras del texto 1 se corresponden con un único
    # elemento del texto 2, entonces los textos son anagramas!!
    else:
        print(" \nSon anagramas --> Sí")


# Si la cantidad de letras no es la misma, 
# entonces automáticamente no son anagramas
else:
    print(" \nSon anagramas --> No")

 



