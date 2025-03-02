#include <iostream>


int main(){
    char eleccion; 
    double numero1;
    double numero2;
    double resultado;
    //ui
    std::cout << "********************Bienvenido a una calculadora en C++**************************\n";
    std::cout<< "ingrese el tipo de calculo desea hacer ( + - * /)\n";
    std::cin >> eleccion; 
     //ingreso de valores
    std::cout << "ingrese el  primer numero: ";
    std:: cin >> numero1;
     std::cout << "ingrese el  segundo numero: ";
     std:: cin >> numero2;
    
    switch(eleccion){
        //divisiones entre 0
        case '+':
        resultado = numero1 + numero2;
        std::cout << "la respuesta de su operacion es: \n" <<resultado; 
        break;
        //caso resta
        case '-':
        resultado = numero1 - numero2;
        std::cout << "la respuesta de su operacion es: \n" <<resultado; 
        break;
        //caso multiplicacion
        case '*':
        resultado = numero1 * numero2;
        std::cout << "la respuesta de su operacion es: \n" <<resultado; 
        break;
        //caso division
        case '/':
        if(numero1, numero2== 0){
        std::cout << "numero = 0, imposible dividir en estas condiciones\n";
        return main();
        }else{
        resultado = numero1 / numero2;
        std::cout << "la respuesta de su operacion es: \n" <<resultado; 
        break;
        }
        //errores
        default:
        std::cout << "Error en la eleccion, reiniciando\n";
        return main();
    }
return 0;

}