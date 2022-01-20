from functools import reduce

def factors(num, limit):  
    '''
    Found the reduce function here: https://stackoverflow.com/questions/6800193
    For all general purposes n and limit should be the same, adjusting the limit may reduce execution time (IE sqrt(num))
    Inner comprehension produces a tuple filled with the factor pairs found using the modulus operation
    Reduce function will apply the given function (in this case it is adding the factor lists) and discards duplicate entries
    '''
    return list(reduce(list.__add__,([i, num//i] for i in range(1,limit+ 1) if num % i == 0)))
