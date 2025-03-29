#Rock paper Scisor en Py

#importes
import random 

#puntuacion
puntuacion = 0
puntuacionMaquina = 0


#ui
def UI():
    print("\n Bienvenido a una prueba de piedra papel o tigera en Python")

#listas de Ramdom.choice
eleccionState = random.randint(0, 1, 2)

#puntuaciones
def resultados():
    print("\n Consideramos el caso de que la maquina tenga 1 en su puntuacion como que perdiste, si la puntuacion tuya es igual a 1 as ganado.")
    print(F"\n Puntuacion {puntuacion} / puntuacion de la maquina {puntuacionMaquina}")
    if puntuacionMaquina == 1:
        print("\nperdiste")
    elif puntuacion == 1:
        print("\n Ganaste")
        return rondanueva()
    
#Nueva ronda
def rondanueva():
    preguntarondanueva = input("\n ejecutar otra ves? jugar? (si/no)")
    #manejo de opciones incorrectas
    if preguntarondanueva.lower() not in ["si" ,"no"]:
        print("\n Error de seleccion, volviendo a preguntar")
        return rondanueva()
    #match
    while True:
        match preguntarondanueva:
            case "si":
                print("\n Reiniciando ronda, las puntuaciones quedaran en 0")
                return juego()
            case "no":
                 print ("\n Gracis por usar nuestro servicio")
                 break

#juego en si
def juego():
    #puntuacion global
    global puntuacion
    global puntuacionMaquina
    #escenarios y casos
    while True: 
        UI()
        Eleccion = input("\ningrese su eleccion: Piedra, papel o tigera")
        #validacion de datos
        if Eleccion.lower() not in ["piedra", "papel", "tigera"]:
            print("Esta es una eleccion no valida, Reiniciando consola...")
            return juego()
        #nodo try
        try:
            match Eleccion: 
            #nodo para piedra
                case "piedra":
                    if random.randint(0,1) == 0: 
                         print("\n Saco tigeras")
                         puntuacion += 1
                         return resultados()    
                         
                    else:
                         print("\n saco papel")
                         puntuacionMaquina += 1
                         return resultados()    
                         
            #nodo para papel
                case "papel":
                     if random.randint(0,1) == 0: 
                         print("\n saco piedra")
                         puntuacion += 1
                         return resultados()    
                         
                     else:
                         print("\n saco tigera")
                         puntuacionMaquina += 1
                         return resultados()    
                           
            #nodo para tigeras
                case "tigera": 
                    if random.randint(0,1) == 0:
                         print("\n saco papel")
                         puntuacion +=1
                         return resultados()    
                         
                    else:
                         print("\n saco piedra")
                         puntuacionMaquina += 1 
                         return resultados()                        
        #gestion de errores
        except ValueError:
            print(F"Esto es un juego de piedra papel o tigera, te voy a reiniciar todo con tu puntuacion actual de: {puntuacion}")
            return juego()
        

juego()
