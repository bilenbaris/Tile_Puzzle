import numpy as np
import heapq

class Agent:
    
    def __init__(self, matrix):
        """
            Initialize the agent.

            Args:
                matrix (list): The initial game matrix
        """
        # The initial game matrix
        self.initial_matrix = [list(row) for row in matrix]
        self.game_size = len(matrix)

        # The desired game matrix
        self.desired_matrix = np.arange(1, self.game_size * self.game_size + 1).reshape(self.game_size, self.game_size)
        self.desired_matrix[-1][-1] = 0
        
        # Large value to represent infinity
        self.INFINITY = 2**32

        # Direction vectors for RIGHT, LEFT, UP, DOWN
        self.directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        # The position of the empty tile
        self.empty_tile = self.find_tile_position(matrix,0)

        # The frontier and explored sets for the search algorithms 
        self.frontier = None
        self.explored = None

        # Information regarding nodes
        self.expanded_node = 0
        self.generated_node = 0
        self.maximum_node_in_memory = 0

        # The total number of moves
        self.total_move = 0
    
    def find_tile_position(self, matrix, tile):
        """
            Returns the position of the empty tile in the current game matrix.

            Args:
                matrix (array): The current game matrix

            Returns:
                tuple (int, int): The position of the empty tile
        """
        for i in range(self.game_size):
            for j in range(self.game_size):
                    if matrix[i][j] == tile:
                        return (i, j)
    
    def checkEqual(self, matrix1, matrix2):
        """
            Check if two matrices are equal.

            Args:
                matrix1 (array): The first matrix
                matrix2 (array): The second matrix

            Returns:
                bool: True if the matrices are equal, False otherwise
        """
        for i in range(self.game_size):
            for j in range(self.game_size):
                if matrix1[i][j] != matrix2[i][j]:
                    return False
        return True
    
    def get_moves(self, Node):
        """
            Returns a list of matrices that represent the solution.

            Args:
                Node (Node): The node to follow the solution path
            
            Returns:
                list: A list of game matrices
        """
        road = [] 
        while Node.parent != None:
            road.append(Node.matrix)
            Node = Node.parent
            self.total_move += 1
        return road[::-1]
                    
class Node():
    
    def __init__(self, parent, position, matrix, g_score = 0, h_score = 0):
        """
            Initialize the node.

            Args:
                parent (Node): The parent node
                position (tuple): The position of the empty tile
                matrix (array): The game matrix
                g_score (int): The g score of the node
                h_score (int): The h score of the node
        """
        self.parent = parent
        self.position = position
        self.matrix = matrix

        self.g_score = g_score
        self.h_score = h_score
        self.f_score = g_score + h_score

    def __lt__(self, other):
        """
            Compare the g and h scores of two nodes.

            Args:
                other (Node): The other node to compare
        """
        return self.g_score > other.g_score or self.h_score > other.h_score
    
class PriorityQueue:

    def __init__(self):
        """
            Initialize the priority queue.
        """
        self.elements = []

    def isEmpty(self):
        """
            Check if the priority queue is empty.

            Returns:
                bool: True if the priority queue is empty, False otherwise
        """
        return len(self.elements) == 0

    def push(self, item, priority):
        """
            Push an item into the priority queue.

            Args:
                item (Node): The item to push
                priority (int): The priority of the item
        """
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        """
            Pop an item from the priority queue.

            Returns:
                Node: The item with the highest priority
        """
        return heapq.heappop(self.elements)[1]

    def size(self):
        """
            Returns the size of the priority queue.

            Returns:
                int: The size of the priority queue
        """
        return len(self.elements)
    
    def contains(self, matrix):
        """
            Check if the priority queue contains the given matrix.

            Args:
                matrix (array): The matrix to check

            Returns:   
                bool: True if the priority queue contains the matrix, False otherwise
        """
        for element in self.elements:
            if element[1].matrix == matrix:
                return True
        return False