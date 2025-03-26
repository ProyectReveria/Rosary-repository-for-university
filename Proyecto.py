#Constantes universales:
##habitacion 1

Disponible0 = True
ospedados0 = 0
precio0 = 40000
diasreservado0 = 0
preciototal = precio0 *diasreservado0
##habitacion 2
Disponible1 = True
ospedados1 = 0
precio1 = 40000
diasreservado1 = 0
preciototal1 = precio1 *diasreservado1
##habitacion 3
Disponible2 = True
ospedados2 = 0
precio2 = 40000
diasreservado2 = 0
preciototal2 = precio2 *diasreservado2

###
#Modulo de reserva
###
def reserva():
    print("Estado actual de las habitaciones: ")
    if Disponible0 == True:
        print("Habitacion disponible")
    else:
        print("habitacion no disponible")
    if Disponible1 == True:
        print("Habitacion disponible")
    else:
        print("habitacion no disponible")
    if Disponible2 == True:
        print("Habitacion disponible")
    else:
        print("habitacion no disponible")

###
#Estado actual de una reservacion
###

def Registro():
    llegada_nueva = int(input("A llegado un cliente nuevo? (1 = si/ 0 = no)"))
    if llegada_nueva == 0:
        print("perfecto!")
    elif llegada_nueva == 1:
        Cambiodeestado = int(input("Si es el cuarto uno el que recibe a los clientes, precione 1 | si es el cuarto dos, precione 2,| si es el cuarto 3, presione 3"))
        if Cambiodeestado == 1:
            Disponible0 = False
            ospedados0 = int(input("Cuantos son los hospedados?"))
            diasreservado0 = int(input("Cuantos dias se hospeda?"))
            print(f"El precio total es{preciototal}")
        elif Cambiodeestado == 2:
            Disponible1 = False
            ospedados1 = int(input("Cuantos son los hospedados?"))
            diasreservado1 = int(input("Cuantos dias se hospeda?"))
            print(f"El precio total es{preciototal1}")
        elif Cambiodeestado == 3:
            Disponible2 = False
            ospedados2 = int(input("Cuantos son los hospedados?"))
            diasreservado2 = int(input("Cuantos dias se hospeda?"))
            print(f"El precio total es{preciototal2}")
