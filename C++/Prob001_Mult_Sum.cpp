//@Author Jared Scott 
//This file contains the logic for solving the first project euler question

#include <iostream>

double CountMultiples(double limit)
{
    int curVal = 0;
    int curSum = 0;
    while (curVal < limit) {
        if (curVal % 3 == 0 || curVal % 5 == 0) {
            curSum = curSum + curVal;
        }
        curVal = curVal + 1;
    }
    return curSum;
}

int main()
{
    std::cout << CountMultiples(1000);
}
