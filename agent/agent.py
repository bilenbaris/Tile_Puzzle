import time

class Agent:
    
    def __init__(self):
        self.expanded_node_count = 0
        self.generated_node_count = 0
        self.maximum_node_in_memory_count = 0