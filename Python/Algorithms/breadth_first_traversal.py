'''
    @Author Jared Scott ☯
    This file sets up a simple graph example using the analogy of towns.
    The function Breadth_First_Traversal demonstrates the BFT algorithm for graph traversal
    When traversed starting from Town A the order of a breadth first traversal shall be the following:
        Town_A  
        Town_B
        Town_D 
        Town_E 
        Town_C 
'''

def main():
    #Main function, defines the town graph and kicks off the recursive traversal function 
    print("Performing a Breadth-First Traversal of the graph...") 
    visited_towns = []
    towns = {
        "Town_A": ["Town_B","Town_D","Town_E"],
        "Town_B": ["Town_A","Town_E"],
        "Town_C": ["Town_D"],
        "Town_D": ["Town_A","Town_C"],
        "Town_E": ["Town_A","Town_B"]
    }
    Breadth_First_Traversal(visited_towns, towns, "Town_A") 
    print("All accessible nodes in graph have been visited")
    
def Breadth_First_Traversal(visited_towns, towns, cur_node):
    #Uses a breadth first traversal pattern to visit all accessible nodes within the provided graph
    visited_towns.append(cur_node)
    to_visit = []
    to_visit.append(cur_node) 
    
    while len(to_visit) > 0:
        active_node = to_visit.pop(0) 
        print("Visiting: " + active_node) 
        for neighbor in towns[active_node]:
            if neighbor not in visited_towns:
                visited_towns.append(neighbor) 
                to_visit.append(neighbor) 

if __name__ == "__main__":
    main()