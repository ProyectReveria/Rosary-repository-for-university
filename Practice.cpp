#include <iostream> 
#include <cmath> 


int main(){

    double a; 
    double b; 
    double c;
//Entrada dato "a"
    std::cout<< "enter data A"; 
    std::cin >> a; 
//Entrada dato "a"
    std::cout<< "enter data b";
    std::cin >>b; 

    a = pow(a , 2); 
    b = pow (b, 2);

//calculos por cmath

    c = sqrt(a+b);

    std::cout<<"la hipotenusa es igual a: " << c; 
    return 0; 
}


// tambien se puede usar C = sqrt(pow(a,2)+pow(b,2)); deberia dar el mismo resultado
