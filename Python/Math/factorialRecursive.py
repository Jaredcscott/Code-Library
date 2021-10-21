'''
    @Author Jared Scott
    This is a recursive factorial function
'''

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num -1)
