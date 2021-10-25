'''
    @Author Jared Scott
    This function will determine weather the given number is a Triangular number, see comments below for furter details on this destinction 
'''

def isTriangular(num): 
	'''
        This function will return a true or false representing whether or not the given number ('num') is a triangle number 
        A number is triangular, if it is the sum of consecutive natural numbers starting with 0
        IE:
            6 : 1 + 2 + 3 = 6
            10: 1 + 2 + 3 + 4 = 10
            15: 1 + 2 + 3 + 4 + 5 = 15
            21: 1 + 2 + 3 + 4 + 5 + 6 = 21
        
        Arguments: 
            (Integer) num: The number which you would like to test
            
        Output:
            True if the number is triangular, or False if the number is not triangular 
    '''
    # Base case 
    if (num < 0): 
        return False
        
    sum = 0
    n = 0
  
    while(sum <= num):  
        sum = sum + n 
        if (sum == num): 
            return True
        n += 1
  
    return False
