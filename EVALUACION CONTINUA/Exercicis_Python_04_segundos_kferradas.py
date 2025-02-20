"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 4
Mostraremos el mensaje: "Conversor de segundos"
A continuación pediremos al usuario una cantidad de segundos.

Le responderemos:
- Si son menos de 60 segundos, mostrará "X segundos son menos de 1 minuto"
- Si es igual o superior a 60 segundos le diremos:
    "X segundos son Y minutos y Z segundos"

Y así para las siguientes unidades de tiempo. Por tanto, si la cantidad de segundos 
supera la hora, le diremos cuantas horas, minutos y segundos son. 
Lo mismo si supera un día o una semana. 

. 
"""
# Alumno: Kevin Ferradas
######## SOLUCIÓN ########

import os
os.system ("cls")

'''
- La idea es usar las equivalencias entre minutos, horas, días y semanas a segundos.
- Usando el bucle if/elif/else, delimitamos las franjas de tiempo: minuto/hora /día / semana.
- Usando los operadores división entera (//) y módulo (%), realizamos las conversiones´
de segundos a minutos,horas,días o semanas, según sea el caso. 

'''



print("Conversor de segundos \n")



try: #intentamos ejecutar el código
    
    #Pedimos al usuario introducir una cantidad de segundos.
    segundos=int(input("Escriba una cantidad de segundos -> "))
    
    # Equivalencias en segundos
    minuto= 60 
    hora= 3600
    dia=86400
    semana=604800
    
    # Si son menos a 1 minuto (60 s.)
    if segundos < minuto:
        print(f"{segundos} segundos son menos de 1 minuto ")

    # Si es igual o superior a 1 minuto pero inferior a 1 hora (3600s.)   
    elif minuto <= segundos < hora:

        # la cantidad de minutos es el cociente (division entera) de segundos/60. 
        minutos_m=segundos // minuto

        # la cantidad de segundos es el residuo (módulo) de segundos/60.
        segundos_m=segundos % minuto 
        print(f"{segundos} segundos son {minutos_m} minutos y {segundos_m} segundos.")

    # Si es igual o superior a 1 hora pero inferior a 1 día (86400 s.) 
    elif  hora <= segundos< dia:

        # la cantidad de horas es el cociente (division entera) de segundos/3600.
        horas_h=segundos//hora
        
        # La cantidad de minutos es el cociente (division entera) del (residuo de segundos)/60.
        # El residuo de segundos es lo que no entró en las horas
        minutos_h=(segundos % hora)//minuto
        
        # la cantidad de segundos es el residuo (módulo) de (residuo de segundos)/60 
        # El residuo de segundos es lo que no entró ni en horas ni en minutos
        segundos_h=(segundos % hora) % minuto
        print(f"{segundos} segundos son {horas_h} horas, {minutos_h} minutos y {segundos_h} segundos.")
    
        
    # Si es igual o superior a 1 día pero inferior a 1 semana (604800 s.) 
    elif dia <=segundos<semana:

        # La cantidad de días es el cociente (division entera) de segundos/86400.
        dias_d=segundos // dia

        # la cantidad de horas es el cociente (division entera) del (residuo de segundos)/3600.
        # El residuo de segundos es lo que no entró en días
        horas_d=(segundos % dia)//hora

        # La cantidad de minutos es el cociente (division entera) del (residuo de segundos)/60.
        # El residuo de segundos es lo que no entró ni en días ni en horas
        minutos_d=((segundos % dia) % hora) // minuto

        # la cantidad de segundos es el residuo (módulo) de (residuo de segundos)/60 
        # El residuo de segundos es lo que no entró ni en días, horas ni en minutos.
        segundos_d=((segundos % dia) % hora) % minuto
        print(f"{segundos} segundos son {dias_d} días, {horas_d} horas, {minutos_d} minutos y {segundos_d} segundos.")
    
    # Si es igual o superior a 1 semana (604800 s.)
    else:

        # La cantidad de semanas es cociente (division entera) de segundos/86400.
        semanas_s=segundos//semana

        # La cantidad de días es el cociente (division entera) del (residuo de segundos)/86400
        # El residuo de segundos es lo que no entró en semanas.
        dias_s=(segundos % semana)//dia

        # La cantidad de horas es el cociente (division entera) del (residuo de segundos)/3600
        # El residuo de segundos es lo que no entró en semanas ni en días.
        horas_s=((segundos % semana) % dia)//hora

        # La cantidad de minutos es el cociente (division entera) del (residuo de segundos)/60
        # El residuo de segundos es lo que no entró en semanas, días ni horas.
        minutos_s=(((segundos % semana) % dia) % hora) // 60

        # la cantidad de segundos es el residuo (módulo) de (residuo de segundos)/60 
        # El residuo de segundos es lo que no entró ni en semanas, días, horas ni minutos.
        segundos_s=(((segundos % semana) % dia) % hora) % 60
        print(f"{segundos} segundos son {semanas_s} semanas, {dias_s} días, {horas_s} horas, {minutos_s} minutos y {segundos_s} segundos.")

# Si el input no es un número entero (Value error), aparece un mensaje de error.
except:
    print("\nDebe introducir los segundos de manera numérica \n")

