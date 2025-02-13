'''
EJERCICIO 10: TABLA DE MULTIPLICAR
Haz un programa que pida al usuario un número 
y muestre la tabla de multiplicar de ese número
desde 1 hasta 10, ambos incluidos
'''
import os
os.system  ("cls")
try:
    numero=int(input("Introduzca un número --> "))
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

except:
    print("Debe introducir un número")