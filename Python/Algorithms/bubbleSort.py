'''
    @Author Jared Scott 
    This function implements the bubble sort algorithm. 
    This function will augment the list which is given as input
'''
def bubbleSort(inputList):
    didSwap = True
    count = 0
    while didSwap:
        didSwap = False
        for i in range(len(inputList) - 1):
            if inputList[i] > inputList[i + 1]:
                inputList[i], inputList[i + 1] = inputList[i + 1], inputList[i]
                count += 1
                print("Swapping...",inputList)
                didSwap = True
    print("Sorting finished\nThe Input List has been altered")
def main():
    list = [3,1,7,4,0,9,6]
    print("BEFORE:",list)
    bubbleSort(list) 
    print("AFTER:",list)

if __name__ == "__main__":
    main()
