def fibonacci(values):
	fibNums = []
	fibNums.append(1) 
	fibNums.append(2) 
	while len(fibNums) < values:
		fibNums.append(fibNums[-2] + fibNums[-1])
		
	return fibNums
    
print(fibonacci(20))