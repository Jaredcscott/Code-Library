'''
    @Author Jared Scott
    This function will return a list of factors for the given number 
'''
def factors(n):
    '''
        This function will return a list containing the factors for the number 'n'. 
        
        Arguments: 
            (Integer) n: The number for which you would like to find the factors
            
        Output:
            A list containing the factors for the specified number
    '''
    results = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i not in results:
                results.append(i)
            if int(n/i) not in results:
                results.append(int(n/i))
    if n in results:
        results.pop(results.index(n))
    return results
