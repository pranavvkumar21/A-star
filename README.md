# A* Algorithm Implementation in Python
This is a Python implementation of the A* algorithm, which is a popular search algorithm used in artificial intelligence and computer science for finding the shortest path between two nodes in a graph.

## Functions
This implementation uses the following functions:

### distance()
This function calculates the Euclidean distance between two elements in the grid map. It takes two arguments, element1 and element2, which are instances of the Element class. It returns a float value representing the distance between the two elements.

### get_neighbors()
This function takes an element and a grid map as arguments and returns a list of all the unexplored neighbors of the element that are not obstructed. It checks the four cardinal directions (up, down, left, and right) and skips any neighbor that is obstructed or already explored. It returns a list of elements.

### get_lowestf()
This function takes a set of elements and a dictionary of f scores as arguments and returns the element in the set with the lowest f score. If multiple elements have the same f score, it returns the one with the lowest g score. It returns an instance of the Element class.

### create_obstruction()
This function takes a grid map and a probability as arguments and randomly changes the status of elements to obstructed with the given probability. It returns nothing.

### reconstruct_path()
This function takes the current element and the starting element as arguments, and uses the g_score dictionary to backtrack through the grid map to construct the path from the starting element to the current element. It returns a list of elements.

### A_star()
This function is the main implementation of the A* algorithm. It takes a grid map, a starting element, and a goal element as arguments and returns a list of elements representing the shortest path from the starting element to the goal element. It initializes the open and closed sets, the g_score and f_score dictionaries, and uses the get_neighbors(), get_lowestf(), and reconstruct_path() functions to explore the grid map and find the shortest path.

## Algorithm Steps
The A* algorithm consists of the following steps:

1. Initialize the open and closed sets. The open set contains the starting element, and the closed set is initially empty.
2. Initialize the g_score and f_score dictionaries. The g_score dictionary stores the actual cost from the starting element to each explored element, and the f_score dictionary stores the estimated total cost from the starting element to each unexplored element through the current element.
3. While the open set is not empty, choose the element in the open set with the lowest f score.
4. If the current element is the goal element, we have found the shortest path. Use the reconstruct_path() function to backtrack through the g_score dictionary to construct the path from the starting element to the current element, and return the path.
5. Move the current element from the open set to the closed set.
6. Explore the neighbors of the current element. For each neighbor that is not obstructed and not already in the closed set:
(-) Calculate the tentative g score for the neighbor.
(-) If the neighbor is not in the open set, add it to the open set.
(-)If the neighbor is already in the open set and the tentative g score is greater than or equal to the current g score, skip the neighbor.
(-)Update the g score and f score for the neighbor.
7. If the goal element cannot be reached, return an empty path.
