'''
EJERCICIO 11: SUMA CONSECUTIVA
Haz un programa que pida al usuario un número comprendido entre 1 y 10
y muestre la suma de todos los números anteriores 
empezando por el 1 y acabando en el propio número del usuario.

Por ejemplo, si escribe 3, 
la operación debe ser 1 + 2 + 3 = 6
Si escribe 5,
la operación debe ser 1 + 2 + 3 + 4 + 5 = 15

'''
import os
os.system ("cls")

numero = int(input ("Escriba un número comprendido entre 1 y 10. --> "))

try:
    suma=0
    lista=[]
    if 1<numero<10:
        for i in range(1,numero + 1):
            suma +=i 
            lista.append(str(i))
            texto = " + ".join(lista)
        print(f"{texto} = {suma}")
    else:
        print ("El número debe estar contenido entre 1 y 10")
except ValueError:
    print ("Debes insertar un número.")


