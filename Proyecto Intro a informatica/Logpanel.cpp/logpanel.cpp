//? include global
#include <iostream>
#include <string.h> 
#include <algorithm>
#include <cctype>
#include <cstring>
//*Lista de char
char user[] ="Empresagenerica.VeigaMarses@gmail.com"; //! cString
char userinput[100]; //! CppString

//? strin bullshit
std::string passcode = "EmpleadoAcceso";
std::string userpasscode; 
//! funcion
int useracces(){
    //!sin esto el codigo no anda.
    //!codigo
    std::cout << "\n Bienvenido a (inserte empresa generica), esta es una aplicacion de la empresa, por favor inserte su usuario";
    std::cout << "\n Por favor introdusca su usuario, si usuario no es valido la consola cerrara";
    std::cin >> userinput;
    //! codigo no anda
    if ((user == userinput)){
    //! codigo no anda
        std::cout << "ocupo la contraseña";
        std::cin >> userpasscode;
        strlwr(userinput);
        strlwr(user);
        if (userpasscode == passcode){
        std::cout<< "bienvenido [usuariogenerico]";
        }else{
            std::cout << "error, cerrando consola";
            return 0;
        }
    }else{
        std::cout << "usuario no reconocido,cerrando consola";
        return 0;
    }
    return 0;
}

//? aun no se puede valorar user

//! me quiero tirar por un puto puente, lenguaje de mierda detectame el maldito Char hijo de puta que te los estoy conparando como C-Char maldito lenguaje del
//!orto puta mierda que sos podes puto funcionar  y detectarme el puto char que tus char tambien estan en C maldito imbecil
//! es un puto char, no tiene mas que al final del dia son el mismo dato en hexadecimal no te jode puto lenguaje del orto
