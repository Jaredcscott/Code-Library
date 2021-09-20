#@author Jared Scott

def fibonacci(values):
    '''
        This function will return a list containing 'values' number of fibonacci numbers. 
        
        Arguments: 
            (Integer) values: the number of fibonacci numbers you would like to generate 
            
        Output:
            A list containing the specified number of fibonacci numbers 
    '''
    fibNums = []
    fibNums.append(1) 
    fibNums.append(2) 
    while len(fibNums) < values:
        fibNums.append(fibNums[-2] + fibNums[-1])
    return fibNums
    
print(fibonacci(20))