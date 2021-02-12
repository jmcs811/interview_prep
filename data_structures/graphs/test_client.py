from graph import Graph
from depth_first_search import DepthFirstSearch
from depth_first_paths import DepthFirstPath

class TestClient:
    graph = Graph()
    graph.load_from_file('./data/tinyG.txt')
    #dfs = DepthFirstSearch(graph, 0)
    dfs = DepthFirstPath(graph, 0)

    def print_path(self, path):
        result = ""
        for i in range(len(path) - 1):
            result = result + f"{path[i]} -> "
        result = result + f"{path[len(path)-1]}"
        return result

test = TestClient()
#print(test.dfs.has_path_to(3))
print(test.dfs.path_to(3))
print(test.print_path(test.dfs.path_to(3)))
#print(test.graph.print_vertices())