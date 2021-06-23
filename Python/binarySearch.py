'''
    @Author Jared Scott 
    This function will return the index of the key if the given key exists within the list.
    If the key does not exist this function will return a string "Key Not Found"
'''

def main():
    list = [2,6,5,7,8,12,34,65,11,77,9,4,32]
    result = binarySearch(122,list)
    if result != "Key Not Found":
        print("Key Found At Index: " + str(result)) 
    else:
        print(result)

def binarySearch(key,list):
    low = 0
    high = len(list) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == list[mid]:
            return mid
        elif key < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
        if high < low: 
            return "Key Not Found" 
            
main()
