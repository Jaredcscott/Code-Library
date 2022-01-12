'''
    @Author Jared Scott ☯
    This file sets up a simple graph example using the analogy of towns.
    The function Depth_First_Traversal demonstrates the DFT algorithm for graph traversal
    When traversed starting from Town A the order of a depth first traversal shall be the following:
        Town_A  
        Town_B
        Town_E 
        Town_D 
        Town_C 
'''

def main():
    #Main function, defines the town graph and kicks off the recursive traversal function 
     print("Performing a Depth-First Traversal of the graph") 
    visited_towns = []
    towns = {
        "Town_A": ["Town_B","Town_D","Town_E"],
        "Town_B": ["Town_A","Town_E"],
        "Town_C": ["Town_D"],
        "Town_D": ["Town_A","Town_C"],
        "Town_E": ["Town_A","Town_B"]
    }
    Depth_First_Traversal(visited_towns, towns, "Town_A") 
    print("All accessible nodes in graph have been visited")
    
def Depth_First_Traversal(visited_towns, towns, cur_node):
    #Uses a depth first traversal pattern to visit all accessible nodes within the provided graph
    if cur_node not in visited_towns:
        print("Visiting: " + cur_node)
        visited_towns.append(cur_node)
        for town in towns[cur_node]:
            Depth_First_Traversal(visited_towns, towns, town) 

if __name__ == "__main__":
    main()