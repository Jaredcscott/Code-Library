//@Author Jared Scott 
//This file contains the logic for solving the first project euler question

#include <iostream>
#include <list> 
using namespace std;
list<int> Fibonacci(double limit)
{
    list<int> vals = {};
    int vala = 1;
    int valb = 2;
    int next = 0;
    int count = 0;
    vals.push_front(1);
    vals.push_front(2);
    while (next <= limit) {
        next = vala + valb;
        vals.push_front(next);
        vala = valb;
        valb = next;
        count++;
    }
    return vals;
}

int main()
{
    list<int> fibNums = Fibonacci(4000000);
    list<int> ::iterator it;
    int sum = 0;
    int curVal;
    std::cout << "Sum of even Fibonacci numbers less than 4,000,000: " << endl;
    for (it = fibNums.begin(); it != fibNums.end(); it++) {
        curVal = *it;
        if (curVal % 2 == 0 ) {
            sum += curVal;
        }    
    }
    std::cout << sum << '\n';
}  
