limit = 1000
    
def countCycleLen(number):
    remainders = [10]
    while ((remainders[-1]) % number)*10 not in remainders:
        remainders.append((remainders[-1] % number)*10)
    return len(remainders)-remainders.index((remainders[-1] % number)*10)    

def solve(limit):
    longest = 0
    cycleLen = 0
    curVal = 2
    for i in range(2,1000):
        if countCycleLen(i) >= cycleLen:
            cycleLen = countCycleLen(i)
            if cycleLen >= longest:
                longest = i
            curVal = i
    return longest

print(solve(limit))