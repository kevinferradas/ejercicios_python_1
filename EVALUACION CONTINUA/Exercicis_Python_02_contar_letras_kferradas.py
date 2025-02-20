"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 2a

Mostraremos el texto: "Contar letras en un texto"

Pediremos al usuario un texto, así:
"Por favor, introduzca un texto "
Puede contener números y caracteres con tilde.

A continuación mostraremos las letras que contiene y cuantas son,
ordenadas por número de apariciones. En caso de empate, en orden alfabético. 
Ignoraremos los números, los espacios y los signos de puntuación 
(punto, coma, punto y coma, exclamación, etc.)
Consideremos mayúsculas y minúsculas como la misma letra.

Por ejemplo:
"Por favor, introduzca un texto " ¿Amar?
La respuesta sería: 
"El texto contiene las letras:
a, 2 veces
m, 1 vez
r, 1 vez
"

Por ejemplo:
"Por favor, introduzca un texto " Python forever and ever
La respuesta sería: 
"El texto contiene las letras:
e, 4 veces
r, 3 veces
n, 2 veces
o, 2 veces
v, 2 veces
a, 1 vez
d, 1 vez
f, 1 vez
h, 1 vez
p, 1 vez
t, 1 vez
y, 1 vez
"
"""
# Alumno: Kevin Ferradas
######## SOLUCIÓN ########

import os
os.system ("cls")

'''
1. La idea es contar el número de apariciones de un cierto caracter (letra) en un texto.

2. Para esto, el programa primero reemplazará cualquier signo de puntuación, espacio
o números, por cadenas vacías.

3. Una vez tengamos todo el texto compacto en una sola cadena, ordenamos las letras del texto de acuerdo al
número de apariciones en el texto, y alfabéticamente en caso de empate, y las almacenamos en una nueva lista. 
Para esto usamos el bucle for y condicionales if/elif . Contamos el número de aparicione utilizando 
el métrodo .count() asociado a los strings.

4. Una vez tengamos la lista ordenada, imprimimos cada elemento con su respectiva cantidad de apariciones.
'''


print("Contar letras en un texto. \n ")

#Pedimos al usuario que introduzca un texto.
texto=input("Por favor, introduzca un texto -> ")


# Definimos una lista con los elementos a ignorar :
# signos de exclamación,signos de interrogación, coma, punto y coma,dos puntos, punto, espacio, números.
signos=["¡","!","¿","?",",",";",":","."," ","0","1","2","3","4","5","6","7","8","9"]

# Cada elemento de la lista "signos" que sea encontrado en el texto
# será reemplazado por un string vacío :""
for signo in signos:
    texto=texto.replace(signo,"") 

# Consideramos mayúsculas y minúsculas como la misma letra.
texto=texto.lower() 

#Consideramos letras con/sin acento como la misma letra.
texto=texto.replace("á","a")
texto=texto.replace("é","e")
texto=texto.replace("í","i")
texto=texto.replace("ó","o")
texto=texto.replace("ú","u")


# ORDENAMOS LAS LETRAS DE ACUERDO AL NÚMERO DE APARICIONES, Y ALFABÉTICAMENTE ( SI HACE FALTA).

# Creamos una lista , inicialmente vacía, que almacenará las letras y las ordenará
# en forma descendente en relación al número de veces que aparece en el texto.
# En caso de empate, primará el orden alfabético.
lista_ordenada=[]

# Iteramos sobre las letras que componen el texto.
for letra in texto:
    
    # Contamos las apariciones de una determinada letra, en el texto.
    contador=texto.count(letra) 


    # Si lista_ordenada tiene al menos un elemento (lista_ordenada = True)
    if lista_ordenada:

        # Este código se ejecuta solo si la letra aún no está en lista_ordenada
        # De esta manera evitamos que la letra se almacene más de 1 vez en lista_ordenada.
        if letra not in lista_ordenada:

            for i in range(len(lista_ordenada)):

                # ordenamos de manera decreciente, en función al número de apariciones.
                if  texto.count(letra) > texto.count(lista_ordenada[i]) :

                    # la letra con mayor número de apariciones desplaza una posición
                    # hacia la derecha a la letra con menor cantidad de apariciones.
                    # El método insert (i,letra) inserta la letra en la posición "i".
                    lista_ordenada.insert(i,letra) 
                    break  
                
                # si el número de apariciones es el mismo, prima el orden alfabético.
                elif texto.count(letra) == texto.count(lista_ordenada[i]) :

                    if letra < lista_ordenada[i]:

                        # la letra "menor", alfabéticamente hablando, desplaza una posición
                        # hacia la derecha a la letra "mayor".
                        lista_ordenada.insert(i,letra)
                        break

            # Si la letra tiene el menor número de apariciones respecto a 
            # los elementos que se encuentran en lista_ordenada,
            # se agrega en la última posición (append)        
            else:
                lista_ordenada.append(letra)
                
    # Si la lista no contiene ningún elemento (lista_ordenada = False)
    else:
        lista_ordenada.append(letra) # agregamos el primer elemento a lista_ordenada
        
# IMPRIMIMOS LAS LETRAS Y LA CANTIDAD DE VECES QUE APARECE EN EL TEXTO

for letra in lista_ordenada:
    contador=texto.count(letra)
    if contador>1: # para letras con varias apariciones

        print(f"{letra}, {contador} veces ")
        
    else: # para letras con una aparición
        print(f"{letra}, {contador} vez ")

  







    














"""  
Ejercicio 2b

Mostraremos el texto: "Contar palabras en un texto"
Lo mismo que el ejercicio anterior, pero con palabras en lugar de letras.
"""

######## SOLUCIÓN ########



''' 
1. La idea es contar el número de apariciones de una cierta palabra en un texto.
Para esto, el programa primero reemplazará cualquier signo de puntuación y números por cadenas vacías.

2. A diferencia del ejercicio 2a, no podemos ignorar los espacios. Si juntamos todo el texto
en una sola cadena, luego no habría forma de diferenciar entre palabras.

3. Luego, usando el método .split() , asociado a los strings,
creamos una lista cuyos elementos son las palabras que conforman el texto.

4. Ordenamos las palabras de la lista de acuerdo al número de apariciones en el texto,
 y alfabéticamente en caso de empate, y las almacenamos en una nueva lista. 
Para esto usamos el bucle for y condicionales if/elif . Contamos el número de aparicione utilizando 
el métrodo .count() asociado a las listas.

5. Una vez tengamos la lista ordenada, imprimimos cada palabra con su respectiva cantidad de apariciones.

'''


print("Contar las palabras en un texto. \n")

#Pedimos al usuario que introduzca un texto.
texto=input("Por favor, introduzca un texto ->  ")

# Definimos una lista con los elementos a ignorar :
# signos de exclamación,signos de interrogación, coma, punto y coma,dos puntos, punto, números.
signos=["¡","!","¿","?",",",";",":",".","0","1","2","3","4","5","6","7","8","9"]

# Cada elemento de la lista "signos" que sea encontrado en el texto, será 
# reemplazado por un string vacío :""
for signo in signos:
    texto=texto.replace(signo,"")

# Consideramos mayúsculas y minúsculas como la misma letra.
texto=texto.lower()

#Consideramos letras con/sin acento como la misma letra.
texto=texto.replace("á","a")
texto=texto.replace("é","e")
texto=texto.replace("í","i")
texto=texto.replace("ó","o")
texto=texto.replace("ú","u")

# Al usar el método split(" "), separamos la cadena en subcadenas que estén separadas por un espacio " " 
# y las almacenamos en una lista.
# Sin embargo, si entre palabra y palabra hay más de un espacio, en la lista se almacenan cadenas vacías: ""
# Usando split(None) descartamos cadenas vacías en la lista resultante.
lista_palabras=texto.split(None)


# ORDENAMOS LAS PALABRAS DE ACUERDO AL NÚMERO DE APARICIONES, Y ALFABÉTICAMENTE ( SI HACE FALTA).

# Creamos una lista , inicialmente vacía, que almacenará las palabras y las ordenará
# en forma descendente en relación al número de veces que aparecen en el texto.
# En caso de empate, primará el orden alfabético.
lista_ordenada=[]

# Iteramos sobre las palabras que componen el texto.
for palabra in lista_palabras:
    
    # Contamos las apariciones de una determinada palabra en el texto.
    contador=lista_palabras.count(palabra) 


    # Si lista_ordenada tiene al menos un elemento (lista_ordenada = True)
    if lista_ordenada:

        # Este código se ejecuta solo si la palabra aún no está en lista_ordenada
        # De esta manera evitamos que la palabra se almacene más de 1 vez en lista_ordenada.
        if palabra not in lista_ordenada:

            for i in range(len(lista_ordenada)):

                # ordenamos de manera decreciente, en función al número de apariciones.
                if  lista_palabras.count(palabra) > lista_palabras.count(lista_ordenada[i]) :

                    # la palabra con mayor número de apariciones desplaza una posición
                    # hacia la derecha a la palabra con menor cantidad de apariciones.
                    # El método insert (i,palabra) inserta la palabra en la posición "i".
                    lista_ordenada.insert(i,palabra) 
                    break  
                
                # si el número de apariciones es el mismo, prima el orden alfabético.
                elif lista_palabras.count(palabra) == lista_palabras.count(lista_ordenada[i]) :

                    if palabra < lista_ordenada[i]:

                        # la palabra "menor", alfabéticamente hablando, desplaza una posición
                        # hacia la derecha a la palabra "mayor".
                        lista_ordenada.insert(i,palabra)
                        break

            # Si la palabra tiene el menor número de apariciones respecto a 
            # los elementos que se encuentran en lista_ordenada,
            # se agrega en la última posición (append)        
            else:
                lista_ordenada.append(palabra)
                
    # Si la lista no contiene ningún elemento (lista_ordenada = False)
    else:  
        lista_ordenada.append(palabra) # agregamos el primer elemento a lista_ordenada


for palabra in lista_ordenada :

    contador=lista_palabras.count(palabra) 

    if contador > 1: #para palabras con varias apariciones.
 
        print(f"{palabra} -> {contador} veces.")

    else: #para palabras con una aparición.
        print(f"{palabra} -> {contador} vez.")
    



