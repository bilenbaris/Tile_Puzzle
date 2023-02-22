import numpy as np
from agent.agent import *

class BFSAgent(Agent):
    def __init__(self, matrix):
        """
            Initialize the BFS agent.

            Args:
                matrix (array): The initial game matrix
        """
        super().__init__(matrix)
    
    def solve(self):
        """
            Solves the game using BFS algorithm.

            Returns:
                list: A list of game matrices that represent the solution.
        """
        self.frontier = []
        self.explored = []

        initialNode = Node(None, self.empty_tile, self.initial_matrix)
        self.frontier.append(initialNode)

        while self.frontier:

            currentNode = self.frontier.pop(0)
        
            for i in self.directions:
                nextPosition = (currentNode.position[0] + i[0], currentNode.position[1] + i[1])

                if (nextPosition[0] < 0) or (nextPosition[0] >= self.game_size) or (nextPosition[1] < 0) or (nextPosition[1] >= self.game_size):
                    continue

                nextMatrix = [list(row) for row in currentNode.matrix]
                nextMatrix[currentNode.position[0]][currentNode.position[1]], nextMatrix[nextPosition[0]][nextPosition[1]] = nextMatrix[nextPosition[0]][nextPosition[1]], nextMatrix[currentNode.position[0]][currentNode.position[1]]
                
                if self.checkEqual(nextMatrix, self.desired_matrix):
                    self.generated_node += 1
                    lastNode = Node(currentNode, nextPosition, nextMatrix)
                    return self.get_moves(lastNode)
                
                if (nextMatrix not in self.explored) and (nextMatrix not in self.frontier):
                    self.generated_node += 1
                    nextNode = Node(currentNode, nextPosition, nextMatrix)
                    self.frontier.append(nextNode)

            self.expanded_node += 1
            self.explored.append(currentNode.matrix)

            if (len(self.frontier) > self.maximum_node_in_memory):
                self.maximum_node_in_memory = len(self.frontier)

class DFSAgent(Agent):
    def __init__(self, matrix):
        """
            Initialize the DFS agent.
        """
        super().__init__(matrix)

    
    def solve(self):
        """
            Solves the game using DFS algorithm.

            Returns:
                list: A list of game matrices that represent the solution.
        """
        self.frontier = []
        self.explored = []
        
        initialNode = Node(None, self.empty_tile, self.initial_matrix)

        self.frontier.append(initialNode)
        while self.frontier:
            dir_queue = []
            currentNode = self.frontier.pop(0)
            
            for i in self.directions:
                
                nextPosition = (currentNode.position[0] + i[0], currentNode.position[1] + i[1])
                if (nextPosition[0] < 0) or (nextPosition[0] >= self.game_size) or (nextPosition[1] < 0) or (nextPosition[1] >= self.game_size):
                    continue

                nextMatrix = [list(row) for row in currentNode.matrix]
                nextMatrix[currentNode.position[0]][currentNode.position[1]], nextMatrix[nextPosition[0]][nextPosition[1]] = nextMatrix[nextPosition[0]][nextPosition[1]], nextMatrix[currentNode.position[0]][currentNode.position[1]]
                
                if self.checkEqual(nextMatrix, self.desired_matrix):
                    self.generated_node += 1
                    lastNode = Node(currentNode, nextPosition, nextMatrix)
                    return self.get_moves(lastNode)
                
                if (nextMatrix not in self.explored):
                    self.generated_node += 1
                    dir_queue.append(Node(currentNode, nextPosition, nextMatrix))

            for i in range(len(dir_queue)):
                self.frontier.insert(0, dir_queue.pop(0)) 

            self.expanded_node += 1
            self.explored.append(currentNode.matrix)

            if (len(self.frontier) > self.maximum_node_in_memory):
                self.maximum_node_in_memory = len(self.frontier)

class AStarAgent(Agent):
    
    def __init__(self, matrix):
        """
            Initialize the A* agent.

            Args:
                matrix (array): The initial game matrix
        """
        super().__init__(matrix)
    
    def heuristic(self, matrix):
        """
            Calculate the heuristic value of the game matrix.

            Args:
                matrix (array): The current game matrix
            
            Returns:
                int: The heuristic value of the game matrix
        """
        h = 0
        for i in range(self.game_size):
            for j in range(self.game_size):
                if self.desired_matrix[i][j] != matrix[i][j]:
                    pos = self.find_tile_position(self.desired_matrix, matrix[i][j])
                    h += np.linalg.norm(np.array(pos) - np.array((i, j)))
        return h

    def solve(self):
        """
            Solves the game using A* algorithm.

            Returns:
                list: A list of game matrices that represent the solution.
        """
        self.frontier = PriorityQueue()
        self.explored = PriorityQueue()

        initialNode = Node(None, self.empty_tile, self.initial_matrix, 0, self.heuristic(self.initial_matrix))
        self.frontier.push(initialNode, initialNode.f_score)

        while not self.frontier.isEmpty():

            currentNode = self.frontier.pop()

            for i in self.directions:
                nextPosition = (currentNode.position[0] + i[0], currentNode.position[1] + i[1])

                if (nextPosition[0] < 0) or (nextPosition[0] >= self.game_size) or (nextPosition[1] < 0) or (nextPosition[1] >= self.game_size):
                    continue

                nextMatrix = [list(row) for row in currentNode.matrix]
                nextMatrix[currentNode.position[0]][currentNode.position[1]], nextMatrix[nextPosition[0]][nextPosition[1]] = nextMatrix[nextPosition[0]][nextPosition[1]], nextMatrix[currentNode.position[0]][currentNode.position[1]]

                next_h_score = self.heuristic(nextMatrix)
                
                if next_h_score == 0:
                    self.generated_node += 1
                    lastNode = Node(currentNode, nextPosition, nextMatrix, currentNode.g_score + 1, next_h_score)
                    return self.get_moves(lastNode)

                elif not (self.explored.contains(nextMatrix) or self.frontier.contains(nextMatrix)):
                    self.generated_node += 1
                    nextNode = Node(currentNode, nextPosition, nextMatrix, currentNode.g_score + 1, next_h_score)
                    self.frontier.push(nextNode, nextNode.f_score)

            self.explored.push(currentNode, 0)
            self.expanded_node += 1

            if (self.frontier.size() > self.maximum_node_in_memory):
                self.maximum_node_in_memory = self.frontier.size()
