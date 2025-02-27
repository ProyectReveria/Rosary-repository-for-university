Costoporproducto = 10 #valor dinero
#user interface
def UI(): 
    print("Estimado cliente ingrese los datos solicitados para hacer su factura")
############################

#reduccion por la cantidad
def Rcantidad(a):
    return a * 0.95

#fidelidad
def fidelitdad(b):
    return b * 0.90

#intento de limpiar codigo como si esto fuera "using namespace std" que se no se recomienda pero me da igual
#def Pfidel():
     #fidelidad = input("usted a comprado aqui antes? (SI/No)").lower() // no funciona, ocupo tenga .strip pero no me as mostrado .strip

#precios 
def precio(c): 
    return (Costoporproducto * c) * 1.15 
############################

def facturacion(): #facturacion 
    while True:
         UI()
         try: 
             cantidad = int(input("cantidad de objetos a comprar"))
             #el precio de los productos para poder hacer los calculos
             cobro = precio(cantidad)
             print(F"este es su total actual sin descuentos con impuestos {cobro}")
             #calculo #1 (hojala borren el token en el compilador de Python.h)
             if cantidad >= 10: 
                 nuevovalor = Rcantidad(cobro)
                 pfidel = input("A comprado aqui antes? (SI/No)").lower() #preguntar por fidelidad
                 if pfidel == "si":
                     Valorfinal = fidelitdad(nuevovalor)
                     print(F"Su total: {Valorfinal}") #Si, me niego a hacertelo repetido el problema no me pide que vuelva
                 else:
                     print (F" su total: {nuevovalor}")
                     
                     
             else: #esto carece de sentido logico para mi, funciona? si, tiene sentido? no, parece magia.
                 pfidel = input("A comprado aqui antes? (SI/No)").lower() #preguntar por fidelidad
                 if pfidel == "si":
                     Valorfinal = fidelitdad(cobro)
                     print(F"Su total {Valorfinal}")
                     break
                 else: 
                     print(F"su total {cobro}") 
                 
             #compila, si no te compila por X o Y, recompila. por raro suene debido a las limitaciones el propio codigo puede presentar errores. 

 #Si, me niego a hacertelo reusable una y otra ves repetido, el problema no me pide que vuelva
         except ValueError:
            print("Su opcion a generado un error en el sistema")


             

facturacion()

#alguien expliqueme esto de parte de la consola:
#PS C:\Users\Uriel\OneDrive\Documentos\GitHub\proyectoReveria\A-Main> & C:/msys64/mingw64/bin/python.exe c:/Users/Uriel/OneDrive/Documentos/GitHub/proyectoReveria/A-Main/Python/Facturacion.py
#PS C:\Users\Uriel\OneDrive\Documentos\GitHub\proyectoReveria\A-Main> & C:/msys64/mingw64/bin/python.exe c:/Users/Uriel/OneDrive/Documentos/GitHub/proyectoReveria/A-Main/Python/Facturacion.py
#Estimado cliente ingrese los datos solicitados para hacer su factura
#cantidad de objetos a comprar 9 
#Este es el precio actual 103.49999999999999
#Estimado cliente ingrese los datos solicitados para hacer su factura
#cantidad de objetos a comprar

#esto es un fload en medio de un int, genial mas razones para no usar python, y si esto se volvio una carta de queja contra un lenguaje inferior a c++.
#enseñen de una ves clases a si meto Rcantidad en una Class Rcantidad y me ahorro medio problema. 
#enseñe "pass" a si me ahorro LA MITAD DEL PROBLEMA. 

#Y si esto esta en my Github personal, Algun problema? 

#Bibligrafias: Por si se pregunta "De donde sacas tanta informacion": https://docs.python.org/3/tutorial/index.html (El manual de python de donde mas?)

#lo peor de esto es que se tiene errores de sintaxis, lo se, pero no puedo hacer mas con lo limitado se tiene enseñado

#nunca e programado con tantas limitaciones, lo odio. 