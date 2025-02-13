'''
EJERCICIO 9: AÑO BISIESTO
Haz un programa que pida al usuario un año y diga si es bisiesto o no
Averigua cual es el criterio
'''
# Un año bisisesto (en el calendario Gregoriano) cumple los siguientes criterios.
# -- Si no es divisible por 4, entonces no es bisiesto
# -- Si es divisible por 4:
#    -- Si no es divisible por 100 , entonces es bisiesto
#    -- Si es divisble por 100:
#       -- si es divisible por 400, entonces es bisiesto
#       -- si no es divisible por 400, entonces no es bisiesto

import os
os.system ("cls")

# try:
#     year = int(input("Ingrese un año --> "))
#     if year%4 != 0:
#         print(f"El año {year} no es bisiesto.")
#     else:
#         if year % 100 !=0:
#             print(f"El año {year} es bisiesto.")
#         else:
#             if year % 400 == 0:
#                 print(f"El año {year} es bisiesto.")
#             else:
#                 print(f"El año {year} no es bisiesto.")

# except ValueError:
#     print("Debes ingresar el año numéricamente.")

#FORMA 2

try:
    year = int(input("Ingrese un año --> "))
    if (year%4 == 0 and year%100 !=0) or year%400 == 0 :
        print(f"El año {year} es bisiesto.")
    else:
        print(f"El año {year} no es bisiesto.")

except ValueError:
    print("Debes ingresar el año numéricamente.")