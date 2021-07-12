
class Puzzle:
    def __init__(self,name,rows):
        self.name = name.strip()
        self.rows = rows 
        self.cols = []
        self.sqrs = []
        self.__extractCols()
        self.__extractSqrs()
       
    def __extractCols(self):
        for col in range(len(self.rows)):
            curCol = []
            for row in self.rows:
                curCol.append(row[col])            
            self.cols.append(''.join(curCol))
        
    def __extractSqrs(self):
        self.sqrs = []
        left, center, right = [], [], []
        for row in range (0,3):
            for col in range(9):
                if col >= 0 and col < 3:
                    left.append(self.rows[row][col]) 
                if col >= 3 and col < 6:
                    center.append(self.rows[row][col])
                if col >= 6 and col < 9:
                    right.append(self.rows[row][col]) 
        self.sqrs.append(''.join(left))
        self.sqrs.append(''.join(center))
        self.sqrs.append(''.join(right))
        left, center, right = [], [], []
        for row in range(3,6):
            for col in range(9):
                if col >= 0 and col < 3:
                    left.append(self.rows[row][col]) 
                if col >= 3 and col < 6:
                    center.append(self.rows[row][col])
                if col >= 6 and col < 9:
                    right.append(self.rows[row][col])
        self.sqrs.append(''.join(left))
        self.sqrs.append(''.join(center))
        self.sqrs.append(''.join(right))
        left, center, right = [], [], []
        for row in range(6,9):
            for col in range(9):
                if col >= 0 and col < 3:
                    left.append(self.rows[row][col]) 
                if col >= 3 and col < 6:
                    center.append(self.rows[row][col])
                if col >= 6 and col < 9:
                    right.append(self.rows[row][col])
        self.sqrs.append(''.join(left))
        self.sqrs.append(''.join(center))
        self.sqrs.append(''.join(right))
        
    def prettyPrint(self):
        print("--------------------------------------------")
        print(self.name)
        countRow = 0
        for row in self.rows:
            countCol = 0
            for val in row:
                print(val,end='')
                countCol += 1
                if countCol % 3 == 0 and countCol != 9:
                    print('|',end='')
            countRow += 1        
            if countRow  % 3 == 0 and countRow  != 9:
                print('\n-----------')
            else:
                print()
                
    def potentialValues(self,row,col):
        potentialValues = ['1','2','3','4','5','6','7','8','9']
        if str(self.rows[row][col]) != "0":
            print("Val Found!","Row: " + str(row), "Col: " + str(col),"Val: " + str(self.rows[row][col]))
            return [self.rows[row][col]]
            
        sqrIndex = self.getSqr(row,col)
        checkRow = self.rows[row] 
        checkCol = self.cols[col]
        checkSqr = self.sqrs[sqrIndex]  
        
        for char in str(checkRow):
            if char in potentialValues:
                potentialValues.remove(char) 
        for char in str(checkCol):
            if char in potentialValues:
                potentialValues.remove(char) 
        for char in str(checkSqr):
            if char in potentialValues:
                potentialValues.remove(char)     
        print("row: " + str(row), "Col: " + str(col),checkRow,checkCol,checkSqr,potentialValues)
                
        return potentialValues
    
    def getSqr(self,row,col):
        if row >= 0 and row < 3:
            if col >= 0 and col < 3: 
                sqrIndex = 0
            elif col >= 3 and col < 6:
                sqrIndex = 1
            elif col >= 6 and col < 9:
                sqrIndex = 2
        elif row >= 3 and row < 6:
            if col >= 0 and col < 3: 
                sqrIndex = 3
            elif col >= 3 and col < 6:
                sqrIndex = 4
            elif col >= 6 and col < 9:
                sqrIndex = 5
        elif row >= 6 and row < 9:
            if col >= 0 and col < 3: 
                sqrIndex = 6
            elif col >= 3 and col < 6:
                sqrIndex = 7
            elif col >= 6 and col < 9:
                sqrIndex = 8
        return sqrIndex
    
    def solvePuzzle(self,times):
        while times > 0:
            for row in range(9):
                for col in range(9):
                    potVals = self.potentialValues(row,col)
                    if len(potVals) == 1:
                        self.updateVal(row,col,potVals[0])
            times -= 1
                    
    
    def updateVal(self,row,col,val):
        #print(self.rows[row][col])
        #print(list(self.rows[row]),col)
        tempList = list(self.rows[row])
        tempList[col] = val
        self.rows[row] = ''.join(tempList)
        
        self.__extractCols() 
        self.__extractSqrs()
    
    def __str__(self):
        return "Name: " + self.name + "\nRows: " + str(self.rows) + "\nCols: " + str(self.cols) + "\nSqrs: " + str(self.sqrs) + "\n\n"


def main():
    puzzles = readPuzzles("C:\\Users\\jscott\\Desktop\\puzzles.txt")
    #for puzzle in puzzles:        
    #    puzzle.prettyPrint()
    puzzles[0].prettyPrint()
    puzzles[0].solvePuzzle(100)
    puzzles[0].prettyPrint()

def readPuzzles(filepath):    
    file = open(filepath,'r')
    lines = file.readlines()
    puzzles = []
    curPuzzle = []
    for line in lines:
        if line[0:4] == "Grid":
            name = line
        else:
            curPuzzle.append(line.strip())
            
        if len(curPuzzle) == 9:
            puzzles.append(Puzzle(name,curPuzzle))
            curPuzzle = []
    return puzzles 
      
      
main()