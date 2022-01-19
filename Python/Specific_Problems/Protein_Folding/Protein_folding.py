class Protein:
    def __init__(self,string):
        self.string = string


def main():
    example = "HHPPHHHPHHPH"
    pro = Protein(example) 
    print(pro.string)



if __name__ == "__main__":
    main()