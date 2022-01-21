class Protein:
    #Class structure to represent a protein and compartmentalize analysis
    def __init__(self,string):
        self.string = string
        self.grid = generate_grid(len(self.string))
        
    def print(self):
        print("Folded protein generated from: " + self.string)
        for row in self.grid:
            print(row)
        
def generate_grid(grid_size):
    '''
    A function which will generate a square grid of the given size 
    All values are initialized to an empty string
    '''
    grid = [["" for j in range(grid_size)] for i in range(grid_size)]
    return(grid)

def main():
    example = "HHPPHHHPHHPH"
    pro = Protein(example) 
    pro.print()
    
if __name__ == "__main__":
    main()