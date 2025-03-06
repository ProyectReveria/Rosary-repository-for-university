//* notas 

//! C tiene un dato estacionado
//? El valor de C da -17.558, ignora pedir el numero


//*notas


#include <iostream>
#include <cctype>

int main(){
    //!temperatura
    double Temperatura; 

    //!respuesta
    char respuesta; 

    std::cout << "\n En que medida esta tu temperatura? Esto es un programa de conversion";
    std::cout << "\n primero ocupamos la temperatura actual";
    std::cin >> Temperatura;
    std::cout << "\n Tome en cuenta que solo trabajamos Fahrenheit y Celsius, cualquier otra respuesta o mala escritura dara un error ";
    std::cin >> respuesta;
    //! forzar Celcius sea C en caso de
    //! Forzar Mayuscula
     respuesta = std::toupper(respuesta);
     //! Forzar Mayuscula

    //* calculos
    //!calculo farenheid
    double Farenhaidtemp = (double (Temperatura* 9/5) +32);
    //!calculo celcius 
    double celciustemp = (double(Temperatura -32)) *5/9;
    //* calculos
    //!switch de caso
    switch (respuesta){
        //!caso Farenheid
        case 'F':
        std::cout << "\n La temperatura es de: " << Farenhaidtemp << " Grados Farenheit"<< std::endl; 
        break;
        //!caso Celcius 
        case 'C':
        std::cout << "\n La temperatura es de: " << celciustemp << " Grados Celsius"<< std::endl; 
        break; 
        //! gestion de errores
        default:
        std::cout << "\n Error, volviendo al inicio";
        break;
    }
return 0; 
}