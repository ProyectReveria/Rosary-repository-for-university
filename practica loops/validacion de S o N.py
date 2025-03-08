
def eleccion():
    while True:
        try:
            print("Bienvenido a un sistema de valoracion")
            Valoracion = input("Ingrese (S / N)").lower()
            if Valoracion == "s":
                print("Valido")
            if Valoracion == "n":
                print("Valido") #valido 2
                break


        except ValueError: 
            print("Eleccion no valida")
        

eleccion()


