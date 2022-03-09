//@Author Jared Scott ☯
//This file contains the logic for converting a Fahrenheit Temperature into Kelvin

#include <iostream>

double ToKelvin(double TempFahrenheit)
{
    double TempKelvin = -1;
    TempKelvin = ((5.0 / 9.0) * (TempFahrenheit - 32.0)) + 273.15;
    return TempKelvin;
}

int main()
{
    std::cout << ToKelvin(85);
    std::cout << "\n";
    std::cout << ToKelvin(95);
    std::cout << "\n";
    std::cout << ToKelvin(105);
}

