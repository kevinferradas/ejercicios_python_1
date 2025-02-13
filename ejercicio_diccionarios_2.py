"""
ENTRADAS DEL CINE

Vamos a crear una app para vender entradas del cine.

Hay tres precios:
- Entrada estándar: 9.00
- Mayores de 65 años (seniors) : 6.90
- Infantiles : 7.20

Se puede vender cualquier cantidad de entradas,
pero los menores siempre deber ir acompañados
de un adulto.

Al finalizar la compra mostraremos las entradas 
y el importe total. 

En cualquier momento hay que poder finalizar el proceso sin que se produzca la compra.

No se puede quitar entradas

"""

import os
os.system ("cls")

# precio por entrada
precio_general = 9
precio_mayores = 6.9
precio_infantil = 7.2




adultos_dic={}
mayores_dic={}
infante_dic={}
# costo_final=[adultos_dic,mayores_dic,infante_dic]
costo_final=[]


while True:
    menu = """
1. Entrada general --> 9.00 euros 
2. Mayores de 65 años --> 6.90 euros
3. Infantiles -->7.20
4. Finalizar la compra
X. Salir
"""
    print(menu)

    opcion = input("Elige tu opcion --> ").strip().lower()
    match opcion:
        case "1": # general

            if adultos_dic:
                cantidad_g = int(input("Cuántas entradas generales deseas? -->"))
                precio_g=cantidad_g*precio_general
                adultos_dic["cantidad"]+=cantidad_g
                adultos_dic["costo_total"] +=precio_g
                
            else:
                cantidad_g = int(input("Cuántas entradas generales deseas? -->"))
                precio_g= cantidad_g*precio_general
                adultos_dic.update({"cantidad":cantidad_g, "costo_total": precio_g })
                costo_final.append(adultos_dic)
                
                
       
    
        case "2": # mayores de 65
            if mayores_dic:
                cantidad_m = int(input("Cuántas entradas para personas mayores de 65 años deseas? -->"))
                precio_m=cantidad_m*precio_mayores
                mayores_dic["cantidad"]+=cantidad_m
                mayores_dic["costo_total"] +=precio_m
                
            else:
                cantidad_m = int(input("Cuántas entradas para personas mayores de 65 años deseas? -->"))
                precio_m= cantidad_m*precio_mayores
                mayores_dic.update({"cantidad":cantidad_m, "costo_total": precio_m })
                costo_final.append(mayores_dic)
                

        case "3": # infantiles
            if adultos_dic or mayores_dic:

                if infante_dic:
                    cantidad_i = int(input("Cuántas entradas infantiles deseas? -->"))
                    precio_i=cantidad_i*precio_infantil
                    infante_dic["cantidad"]+=cantidad_i
                    infante_dic["costo_total"] +=precio_i
                
                else:
                    cantidad_i = int(input("Cuántas entradas infantiles deseas? -->"))
                    precio_i= cantidad_i*precio_infantil
                    infante_dic.update({"cantidad":cantidad_i, "costo_total": precio_i })
                    costo_final.append(infante_dic)
                
            else:
                print("Los menores siempre deben ir acompañados de un adulto.")

        case "4":
            if costo_final:
                print(f"Entradas generales--> {adultos_dic["costo_total"]} euros.")
                print(f"Entradas mayores de 65 años --> {mayores_dic["costo_total"]} euros.")
                print(f"Entradas infantiles--> {infante_dic["costo_total"]} euros.")
                suma=0
                for diccionarios in costo_final:
                    suma+=diccionarios["costo_total"]
                print(f"El precio a pagar es {suma} euros")
                print(f"¿Desea finalizar la compra?")
                print("1.Sí\n2.No")
                option=input("Escriba la opción que desea efectuar -->")
                if option == "1":
                    print("Gracias por su compra")
                    break
                else:
                    pass
            
            else:
                print("No tiene ninguna entrada seleccionada.")

        case "x": #salir de la aplicación sin finalizar la compra
            print("Fin del programa")
            break
        case _ :
            print("Opción no reconocida.\nVuélvelo a probar.")

