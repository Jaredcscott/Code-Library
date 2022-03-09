//@Author Jared Scott 
//This file contains the logic for converting a Fahrenheit Temperature into Rankine

#include <iostream>
double FToRankine(double FTemp) 
{
    return FTemp + 459.67;
}

int main()
{
    std::cout << FToRankine(35);
    std::cout << "\n";
    std::cout << FToRankine(42);
    std::cout << "\n";
    std::cout << FToRankine(0);
}
