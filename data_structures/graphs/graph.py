import os

class Graph:
    def __init__(self, v=0):
        '''
        Create a graph object with v nodes
        Use addEdge() to create edges between nodes
        or create an empty Graph object and use 
        load_from_file() to create your nodes and edges
        '''
        self.vertices = v
        self.edges = 0
        self.adj_list = {}

        # create the nodes
        if v != 0:
            self.createGraph(v)

    def createGraph(self, v: int) -> None:
        '''
        Creates v nodes
        '''
        self.vertices = v
        for i in range(self.vertices):
                self.adj_list[i] = []

    def load_from_file(self, file: str) -> None:
        '''
        Reads a file for the node and edge information
        first number in file is number of nodes
        second number in file is number of edges
        following lines contain two numbers dipicting
        the edge between two nodes

        ex:
        13
        13
        0 1
        5 7
        ...
        '''
        self.vertices = 0
        self.edges = 0
        file_path = os.path.abspath(os.path.dirname(__file__)) + file
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                v = int(lines[0])
                e = int(lines[1])
                self.createGraph(v)
                for i in range(2, len(lines)):
                    nums = lines[i].split(' ')
                    self.addEdge(int(nums[0]), int(nums[1]))
        except Exception as e:
            print(e)

    def addEdge(self, v: int, w: int) -> None:
        self.adj_list[w].append(v)
        self.adj_list[v].append(w)
        self.edges += 1
    
    def print(self) -> None:
        print(self.adj_list)

    def print_vertices(self) -> int:
        return self.vertices
    
    def print_edges(self) -> int:
        return self.edges

# test = Graph()
# test.load_from_file('./data/tinyG.txt')
# test.print()
# print(test.print_vertices())
# print(test.print_edges())
