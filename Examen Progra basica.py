

#entorno pensado para un unico estudiante, si ocupa dos solamente agrege la constante 
#nota1A y Nota1B para agregar a un segundo y a si susesibamente
def promedioc(a,b):
    promedio = (a + b)/2 
    return promedio

def UI(): 
    print("bienvenido a el panel de calculo para un solo estudiante")
    print("ahora se pediran las notas")


def promedio():
    while True:
        UI()
        try:
            notaA = float(input("ingrese nota1"))
            notaB = float(input("nota b"))
            if promedioc(notaA, notaB) >= 70:
                print(F"el estudiante esta aprobado con nota de {promedioc(notaA,notaB)}")
                break
            else:
                print(F"el estudiante esta reprobado con nota de {promedioc(notaA,notaB)}")
                break

        except ValueError:
            print("error,reiniciando")

promedio()






    
   
