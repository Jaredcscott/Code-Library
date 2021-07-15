def main():
    ATTEMPTS = 150
    SOLUTIONS_FILEPATH = "C:\\Users\\jscott\\Desktop\\Code-Library\\Python\\Specific_Problems\\Sudoku_Solver\\solutions.dat"
    PUZZLES_FILEPATH = "C:\\Users\\jscott\\Desktop\\Code-Library\\Python\\Specific_Problems\\Sudoku_Solver\\puzzles.txt"
    
    solutions = loadSols(SOLUTIONS_FILEPATH)
    print(len(solutions)," Solutions Loaded")
    if len(solutions) == 0:
        for i in range(1,51):
            solutions[i] = False
    puzzles = readPuzzles(PUZZLES_FILEPATH)
    for puzzle in puzzles:
        #puzzle = puzzles[1]
        puzStr = puzzle.name.split(" ")[1].strip(' "\'\t\r\n')
        puzNum = int(puzStr)
        if str(solutions[puzNum]).strip(' "\'\t\r\n') == "False": 
            print("\nAttempting: " + puzzle.name)
            puzzle.startRecursion()
            puzzle.prettyPrint()
            if puzzle.isSolved():
                
                solutions[puzNum] = puzzle.digits
        
    
    solved = 0
    for puzzle in solutions:
        result = solutions[puzzle]
        if str(result).strip() != "False":
            
            solved += 1 
            
    print("\n" + str(solved) + "/50 Puzzles Solved!")
    file = open(SOLUTIONS_FILEPATH,"wt")
    for solution in solutions:
        file.write(str(solution) + ":" + str(solutions[solution]).strip(' "\'\t\r\n') + "\n")
    file.close() 
    
class Puzzle:
    def __init__(self,name,rows):
        self.name = name.strip()
        self.rows = rows 
        self.cols = self.__extractCols()
        self.sqrs = self.__extractSqrs()
        self.digits = ""
       
    def __extractCols(self):
        cols = []
        for col in range(len(self.rows)):
            curCol = []
            for row in self.rows:
                curCol.append(row[col])            
            cols.append(''.join(curCol))
        return cols 
        
    def __extractSqrs(self):
        sqrs = []
        left, center, right = [], [], []
        for row in range (0,3):
            for col in range(9):
                if col >= 0 and col < 3:
                    left.append(self.rows[row][col]) 
                if col >= 3 and col < 6:
                    center.append(self.rows[row][col])
                if col >= 6 and col < 9:
                    right.append(self.rows[row][col]) 
        sqrs.append(''.join(left))
        sqrs.append(''.join(center))
        sqrs.append(''.join(right))
        left, center, right = [], [], []
        for row in range(3,6):
            for col in range(9):
                if col >= 0 and col < 3:
                    left.append(self.rows[row][col]) 
                if col >= 3 and col < 6:
                    center.append(self.rows[row][col])
                if col >= 6 and col < 9:
                    right.append(self.rows[row][col])
        sqrs.append(''.join(left))
        sqrs.append(''.join(center))
        sqrs.append(''.join(right))
        left, center, right = [], [], []
        for row in range(6,9):
            for col in range(9):
                if col >= 0 and col < 3:
                    left.append(self.rows[row][col]) 
                if col >= 3 and col < 6:
                    center.append(self.rows[row][col])
                if col >= 6 and col < 9:
                    right.append(self.rows[row][col])
        sqrs.append(''.join(left))
        sqrs.append(''.join(center))
        sqrs.append(''.join(right))
        return sqrs
        
    def prettyPrint(self):
        print(self.name,"\nRemaining Empty Spaces: ",self.countEmpty())
        
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
            #print("Val Found!","Row: " + str(row), "Col: " + str(col),"Val: " + str(self.rows[row][col]))
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
        #print("row: " + str(row), "Col: " + str(col),checkRow,checkCol,checkSqr,potentialValues)
                
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
        time = 0
        emptySpaces = 81
        while time < times:
            for row in range(9):
                for col in range(9):
                    potVals = self.potentialValues(row,col)
                    if len(potVals) == 1:
                        self.updateVal(row,col,potVals[0])
            #self.fillSingles()   
            if self.countEmpty() == 0:
                print("Puzzle Solved!")
                self.digits = self.rows[0][:3]
                return
            left = self.countEmpty()
            if left < emptySpaces:
                emptySpaces = left 
                print("Empty Spaces: ",left)
            time += 1
            #if time % 50 == 0:
            #    print("Solving ...")
            
            #if time == times:
            #    print("No Solution Found After " + str(times) + " Attempts")   
    
    def startRecursion(self):
        puzzleState = {}
        for row in range(9):
            for col in range(9):
                puzzleState[(row,col)] = [self.rows[row][col]]
        self.solveRecursive(puzzleState)
    
    def solveRecursive(self, puzzleState):
        if self.isSolved():
            print("-----------------------------------------------------SOLUTION FOUND")
            puzzle.prettyPrint()
            return True
        else:    
            queue = self.getEmptyCells()
            for cell in queue:
                puzzleState[cell] = self.potentialValues(cell[0],cell[1])
            for cell in puzzleState:
                nums = puzzleState[cell]
                if len(nums) > 1:
                    for num in nums:
                        temp = self.getCellVal(cell[0],cell[1])
                        self.updateVal(cell[0],cell[1],num)
                        puzzleState[cell] = str(num)
                        if self.solveRecursive(puzzleState):
                            return True
                        else:
                            return False
                        self.updateVal(cell[0],cell[1],temp)
                elif len(nums) == 0:
                    print(cell)
                else:
                    self.updateVal(cell[0],cell[1],nums[0])
            return False         
            
    def getEmptyCells(self):
        cells = []
        for row in range(9):
            for col in range(9):
                curRow = self.rows[row]
                if curRow[col] == '0':
                    cellLoc = (row,col)
                    cells.append(cellLoc)
        return cells

    def getCellVal(self,row,col):
        return self.rows[row][col]
            
    def tempStorage(self):        
        self.prettyPrint()
        lowestNeed = 9
        lowestInx = 0
        inx = 0
        for sqr in self.sqrs:
            need = 9 - len(self.contains(sqr))
            if need < lowestNeed:
                lowestNeed = need 
                lowestInx = inx
            inx += 1
        self.needs(self.sqrs[lowestInx])
        self.reduceSqr(2)
        #print(self.potentialValues(0,8))
        #print("Need: " + str(lowestNeed) + " Sqr: " + str(lowestInx))
        self.contains(self.sqrs[0])            
    
    def contains(self,vals):
        nums = []
        for val in vals:
            if val not in nums and val != '0':
                nums.append(val)
        return nums
    
    def needs(self,vals):
        nums = ['1','2','3','4','5','6','7','8','9']
        for val in vals:
            if val in nums:
                nums.remove(val)
        return nums
    
    def updateVal(self,row,col,val):
        tempList = list(self.rows[row])
        tempList[col] = val
        self.rows[row] = ''.join(tempList)
        self.cols = self.__extractCols() 
        self.sqrs = self.__extractSqrs()
        
    def countEmpty(self):
        emptyCount = 0
        for row in self.rows:
            line = str(row)
            for char in line:
                if char == '0':
                    emptyCount += 1
        return emptyCount
        
    def isSolved(self):
        if self.countEmpty() == 0:
            return True 
        else:
            return False 
            
    def __str__(self):
        return "Name: " + self.name + "\nRows: " + str(self.rows) + "\nCols: " + str(self.cols) + "\nSqrs: " + str(self.sqrs) + "\n\n"

def loadSols(filepath):
    solutions = {}
    file = open(filepath,"r")
    data = file.readlines()
    if len(data) > 1:
        for solution in data:
            curSol = solution.split(":")
            solutions[int(curSol[0])] = curSol[1]
    return solutions   

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
    file.close()
    return puzzles 
      
main()
