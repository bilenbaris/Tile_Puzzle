import time
import numpy as np
import queue
import heapq

from agent.agent import Agent

class PriorityQueue:

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Node():
    
    def __init__(self, parent, position, matrix, g_score, h_score):
        self.parent = parent
        self.position = position
        self.matrix = matrix
        self.g_score = g_score
        self.h_score = h_score
        self.f_score = g_score + h_score

class AStarAgent(Agent):
    
    def __init__(self, game_matrix):
        super().__init__()

        self.game_matrix = np.array(game_matrix)
        self.size = self.game_matrix.shape[0]

        self.desired_matrix = np.arange(1, self.size * self.size + 1).reshape(self.size, self.size)
        self.desired_matrix[-1][-1] = 0

        # Large value to initialize the g score
        self.INFINITY = 2**10

        # Direction vectors for RIGHT, LEFT, UP, DOWN
        self.directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        # g scores for A* algorithm
        self.g_scores = []
    
    def find_empty_tile(self, game_matrix):
        """
            Find the empty tile in the game matrix.
            return: (row, col)
        """
        for i in range(self.size):
            for j in range(self.size):
                if game_matrix[i][j] == 0:
                    return i, j
    
    def heuristic(self, matrix):
        """
            Calculate the heuristic value of the game matrix.
            return: heuristic value
        """
        h = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.desired_matrix[i][j] != matrix[i][j]:
                    h += 1
        return h
    
    def get_f_score(self, Node):
        return Node.f_score
    
    def get_moves(self, Node):
        road = [] 
        while Node.parent != None:
            road.insert(0, Node.matrix)
            # before_pos = Node.parent.position
            # move = [before_pos[0] - Node.position[0], before_pos[1] - Node.position[1]]

            # if move == self.directions[0]:
            #     road.insert(0,"L")
            # elif move == self.directions[1]:
            #     road.insert(0,"R")
            # elif move == self.directions[2]:
            #     road.insert(0,"D")
            # elif move == self.directions[3]:
            #     road.insert(0,"U")

            Node = Node.parent
        
        return road

    
    def solve(self):
        """
            Solve the game using A* algorithm.
        """

        initial_matrix = [list(row) for row in self.game_matrix]

        self.g_scores = [[self.INFINITY for i in range(self.size)] for j in range(self.size)]

        position = self.find_empty_tile(self.game_matrix)
        self.g_scores[position[0]][position[1]] = 0

        initial_heuristic = self.heuristic(self.game_matrix)



        queue = []
        visited = []
        nodes_in_queue = []
        finished = False

        initial_node = Node(None, position, initial_matrix, 0, initial_heuristic)

        queue.append(initial_node)

        while queue and not finished:

            queue.sort(key=self.get_f_score)

            current_node = queue.pop(0)

            self.expanded_node_count += 1
            current_pos = current_node.position
            current_matrix = current_node.matrix

            for i in self.directions:
                next_pos = (current_pos[0] + i[0], current_pos[1] + i[1])
                
                if next_pos[0] < 0 or next_pos[0] >= self.size or next_pos[1] < 0 or next_pos[1] >= self.size:
                    continue
                
                new_matrix = [list(row) for row in current_matrix]
                new_matrix[current_pos[0]][current_pos[1]] = current_matrix[next_pos[0]][next_pos[1]]
                new_matrix[next_pos[0]][next_pos[1]] = 0
            
                new_h_score = self.heuristic(new_matrix)
                if new_h_score == 0:
                    
                    new_g_score = self.g_scores[current_pos[0]][current_pos[1]] + 1
                    
                    if self.g_scores[next_pos[0]][next_pos[1]] > new_g_score:
                        self.g_scores[next_pos[0]][next_pos[1]] = new_g_score

                    last_node = Node(current_node, next_pos, new_matrix, new_g_score, new_h_score)
                    self.generated_node_count += 1
                    finished = True
                
                elif new_matrix not in visited:

                    new_g_score = self.g_scores[current_pos[0]][current_pos[1]] + 1

                    if self.g_scores[next_pos[0]][next_pos[1]] > new_g_score:
                        self.g_scores[next_pos[0]][next_pos[1]] = new_g_score
                    

                    if new_matrix not in nodes_in_queue:
                        new_node = Node(current_node,next_pos, new_matrix, new_g_score,new_h_score)
                        queue.append(new_node)
                        nodes_in_queue.append(new_matrix)
                        self.generated_node_count += 1

            visited.append(current_matrix)

            if (len(queue) > self.maximum_node_in_memory_count):
                self.maximum_node_in_memory_count = len(queue)

        return self.get_moves(last_node)
