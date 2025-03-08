#defUIser
User = "Empresagenerica.VeigaMarses@musica.com".lower()
UserName = "Veiga Marses"
Passcode = "EmpleadoAcceso"

#def userinput 
userinput = input ("Ingrese su usuario").lower()
passcodeinput = input("Ingrese su contraseña")

#Definventario (Todo lo relacionado al inventario)
Laptops = 2
Mouses = 4
Teclados = 6
Audífonos  = 8
computadoras_de_escritorio = 10

#funcion
def iniciosesion():
    print("Bienvenido al sistema de facturacion de la empres (Inserte nombre generico aqui) por favor introdusca sus datos")
    userinput()

class inventario():

    def stock(self):
        print("Este es el inventario actual")
        userinput
        if userinput == User:
            print(F"usuario{UserName}")

 
def userconsole():
    while True:
        iniciosesion()
