'''
    @Author Jared Scott ☯
    This function will calculate the factorial of the given number
'''
def factorial(n):
    #This function implements the factorial operation namely:
	# example: 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r
    
    
def helperFunc(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
