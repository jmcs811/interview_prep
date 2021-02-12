from graph import Graph

class DepthFirstPath:
    def __init__(self, G: Graph, s: int):
        '''
        Simple DFS using recursion
        Given a graph and a node,
        recursivly visit each node 
        connected to the given node, marking the 
        ones we visit in marked[]

        Also store the "parent" of the node in edgeTo[]
        This allows us to determine the path to any node 
        from s and print the path from s to v
        '''
        self.graph = G
        self.s = s
        self.marked = [False] * self.graph.print_vertices()
        self.edgeTo = [0] * self.graph.print_vertices()
        self.dfs(self.graph, self.s)

    def dfs(self, g, v):
        self.marked[v] = True
        for w in g.adj_list[v]:
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(g, w)
        
    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if self.marked[v] == False:
            return None
        answer = []
        x = v
        while x != self.s:
            answer.append(x)
            x = self.edgeTo[x]
        answer.append(self.s)
        return answer
