'''
    @Author Jared Scott ☯
    This script will identify a single pythagorean triple, whose sum (a+b+c) is 1000. 
    A Pythagorean triple is a set of numbers with this relationship a^2 + b^2 = c^2
'''

def main():
    count = 100
    triplets = []
    a = 0
    b = 0
    c = 0
    sumOfNums = 0
    product = 1
    while sumOfNums != 1000:
        count += 1
        for k in range(1,count + 1):
            a = k
            for i in range(1,count + 1):
                b = i
                for j in range(1,count + 1):
                    c = j
                    if (a*a) + (b*b) == (c*c) and a < b and b < c:
                        if (a,b,c) in triplets:
                            continue
                        triplets.append((a,b,c))
                        print("Pythagorean Triplet found, testing product")
                        print("a: " + str(a) + "\nb: " + str(b) + "\nc: " + str(c))                     
                        #print(triplets)
                        product = a * b * c
                        sumOfNums = a + b + c 
                        print("Sum Of Nums : " + str(sumOfNums)) 

    print("finished!")
    print("a: " + str(a) + "\nb: " + str(b) + "\nc: " + str(c))
    print(product)
    print(triplets)
    
if __name__ == '__main__':
    main()
