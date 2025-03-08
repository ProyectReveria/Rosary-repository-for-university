def menu():
    print("Bienvenido al menu!!")
    print("Si desea ver el mensaje ingrese 1")
    print("Si desea salir ingrese 2")

def main():
    while True:
        try:
            menu()
            Valoracion = input("Cual es tu eleccion?")
            if Valoracion == 1: 
                print("miau miau ! mensaje miau")
                eleccion_mensaje = int("si quiere continuar precione 1, caso contrario precione 2")
                if eleccion_mensaje == 2:
                    print("Gracias por usar mi servicio")
                    break
            if Valoracion == 2:
                    print("Gracias por usar mi servicio")
                    break

        except ValueError: 
            print("Error")

main()

