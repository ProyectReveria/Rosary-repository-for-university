//? include global
#include <iostream>
#include <string.h> 
#include <algorithm>
#include <cctype>

//*Lista de char
char user[] ="Empresagenerica.VeigaMarses@gmail.com";
char userinput[];

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
    //! sin esto el codigo no anda
    if (user == userinput){
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