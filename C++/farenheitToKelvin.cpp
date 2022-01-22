#include <iostream>

double ToKelvin(double pTemperature)
{
    double fTempKelvin = -1;
    fTempKelvin = ((5.0 / 9.0) * (pTemperature - 32.0)) + 273.15;
    return fTempKelvin;
}

int main()
{
    std::cout << ToKelvin(85);
    std::cout << "\n";
    std::cout << ToKelvin(95);
    std::cout << "\n";
    std::cout << ToKelvin(105);
}
