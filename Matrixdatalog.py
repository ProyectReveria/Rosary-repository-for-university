#blockeo de data
A = 2
B = int(0)
C = 1
#blockqueo de datos
D = 3
E = int(0)
F = 4
#blockeo de Miau

inbase =[A,B,C,0]   
inbase2 =[D,E,F,0]


def ACD():
    while inbase: 
        AC = inbase[0]
        DC = inbase[2]
        A = DC
        C = AC
        print(inbase[0])
        print(inbase[2])

def rotacionDatos():
    while inbase and inbase2:
        A = inbase2.append(input("Introdusca un valor agregado a esta cadena"))
        A = inbase
        if inbase2[0] %2 == 0 or inbase2[1] %2 == 0 or inbase2[2] %2 == 0:
            inbase[3] = int(2)
            inbase.append(6)
            print(f"nuevo dato == {inbase[4]}")
            print(f"valor 3 en cadena 1 = {inbase[3]}")
        else: #caso de match inbase[i] e inbase2[i] es mas eficiente a nivel de datos
            inbase[3] = int(3)
            print(f"valor 3 en cadena 1 = {inbase[3]}")
        if inbase[0] == inbase2[0] or inbase[1] == inbase2[1] or inbase[2] == inbase2[2]:
            inbase2[1] and inbase[1] == 3
            print(f"valores {inbase2[1]} ... valores2 {inbase[1]}")
        if inbase[3] == 2 or 3:
            break
        
rotacionDatos()