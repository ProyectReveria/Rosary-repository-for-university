#Temporal Users

########################################## User temporal data info
User = "Empresagenerica@gmail.com".lower()
passcode = "EmpresaGeneica"
#####################################################
# menu                                              #
#####################################################
def menu():
    print("\n Bienvenido a (inserte empresa generica)")
    print("\n si desea inicias secion precione 1")
    print("\n si desea salir precione 2")

######################################################
# stock test Actual                                  #
######################################################
LAPTOPS_CANTIDAD = 10
MOUSES_CANTIDAD = 15
TECLADOS_CANTIDAD = 15
AUDIFONOS_CANTIDAD = 12
COMPUTADORAS_ESCRITORIO_CANTIDAD = 8
################################################
# funcion main, aqui deberia estar alojado todo#
################################################
def main():
    while  True:
        menu()
        try:
            ######### user decition
            Eleccion = int(input("Esperando instruccion"))
            if Eleccion == 1:
                Userinput = input("Por favor ingrese su usuario").lower()
                #validacion de usuario
                if Userinput == User:
                    inputpasscode = input("Por favor ingrese su contraseña")
                    #contraseña
                    if inputpasscode == passcode:
                        print("Bienvenido usuario")
                    else:
                        print("Contraseña incorrecta")
                else:
                    print("Usuario no valido")
            if Eleccion == 2:
                print("Apagando Sistema")
                break
        except ValueError:
            print("Error en la introduccion de datos")
            break
    ############################################################
    #funcion inventario, aqui deberia estar alojado la central #
    ############################################################

def inventario_main():
    print("Inventario actual:")
print(f"Laptops: {LAPTOPS_CANTIDAD}")
print(f"Mouses:  {MOUSES_CANTIDAD}")
print(f"Teclados: {TECLADOS_CANTIDAD}")
print(f"Audifonos: {AUDIFONOS_CANTIDAD}")
print(f"Computadoras de escritotio: {COMPUTADORAS_ESCRITORIO_CANTIDAD}")
# deberia poder introducir la parte Fatalis, Fatalis deberia poder arreglarla en caso de error en el citado.
#notas no importantes (OSea putiar al lenguaje (si esto esta en las notas finales de entrega recuerden, solo es la rabia de un programador))
#Me explican porque mierda no puedo importar un importe?


#nota para Miaurziso:
#Falta conectar archivos y refactorio.
