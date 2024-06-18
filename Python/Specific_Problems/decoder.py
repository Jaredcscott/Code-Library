'''
    @Author Jared Scott ☯
    This file provides a method for decoding a message found by arranging provided data into a pyramid, 
    then combining the final entry for each row of the pyramid into a sentence. If the message file's contents are: 
    3 love
    6 computers
    2 dogs
    4 cats
    1 i
    5 you
    This process will construct a pyramid with the numeric values in the following format: 
      1 
     2 3
    4 5 6
    By combining the last elements in each row, (1, 3 and 6) we get the final decoded message of i love computers 
'''

def main():
    message_file = "coding_qual_input.txt" #Adjust this string in order to decode different files 
    return decode(message_file)            #Decoding the file provided and returning results 
    

def decode(message_file): 
    message = ""                           #This will be the final return value 
    file = open(message_file,'r')          #Reading in the file 
    lines = file.readlines()               #extracting lines into a list 
    sorted_lines = sort_lines(lines)       #Sorting lines by their indicated number 
    words = []                             #Stores the last elements from each row 
    rowCounter = 1                         #Used to fill each row with the right number of elements 
    while len(sorted_lines) > 0:           #Pop method is used to reduce the source list until empty
        row = []                           #Each row will be an array of values 
        for i in range(rowCounter):        #Each row has the same number of elements as the row number row 1 has 1 element, row 2 has 2 elements ...
            row.append(sorted_lines.pop()) #Adding lines to the current row up to the row number 
        words.append(row[-1])              #Adding the last element from the row into the words list
        rowCounter += 1                    #incrementing row count 
    
    for item in words:
        word = item.split(" ")[-1]         #splitting the data using the " " as a delimiter then taking the last index which is the word
        message += word.strip() + " "      #striping the newline char and adding a space  
        
    return message
    
def sort_lines(list):
    sorted_list = [-1] * len(list) 
    for line in list:                       #Scanning through list to sort by number 
        index = int(line.split(" ")[0]) - 1 #Creating an index with the lines number
        sorted_list[index] = line           #Adding in the line at the index location 
    sorted_list.reverse()                  #Reversing list so the .pop() method can be used
    return sorted_list
    
if __name__ == "__main__":
    main()