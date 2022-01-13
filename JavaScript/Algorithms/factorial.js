/*
 *@Author Jared Scott ☯
 *This script is an implementation of the factorial function using recursion
 */

function factorial(num) {
    if (num === 0) {
        return 1;
    }
    return num * factorial(num - 1); 
}

console.log(factorial(10))