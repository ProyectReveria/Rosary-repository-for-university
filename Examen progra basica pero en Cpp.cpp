#include <iostream>
#include <cmath>



int main(){
    double nota1;
    double nota2;
    std::cout << "bienvenido al sistema de notas, ahora en C++"; 
    std::cout << " introdusca la primera nota";
    std::cin >> nota1;
    std::cout << "introdusca nota2"; 
    std::cin >> nota2; 
    double promedio = (nota1+nota2)/2; 
    std::cout << "aqui esta el promedio " << promedio; 

    if (promedio >= 70){
        std::cout << "+Estudiante aprobado";
    }else{
        std::cout << "-estudiante reprobado";
    }
    return 0; 
}
