'''
    @Author Jared Scott 
    This function will sort the given list of integers
'''

def main():
    list = [2,6,5,7,8,12,34,65,11,77,9,4,32]
    if type(list[0]) != type(1):
        print("Invalid list elements\nList must contain integers")
    else:    
        print("Before: " + str(list))
        selectionSort(list)
        print("After: " + str(list))   

def selectionSort(list):
    #This function sorts the list. 
    #NOTE: The original list has been modified
    for i in range(len(list)):
        minIndex = i
        for j in range(i+1,len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex],list[i]
    
main()