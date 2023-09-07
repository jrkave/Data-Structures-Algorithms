# Graphs: Topological Sort

class Graph(object):
    
    def __init__(self, graph):
        self.graph = graph
        
    def topSort(self):
        visited = set()
        stack = []
        
        for node in self.graph.keys():
            if node not in visited:
                self.dfs(node, visited, stack)
        
        return stack[::-1] # return reversed stack
        
    
    def dfs(self, node, visited, stack):
        visited.add(node)
        for neighbor in self.graph[node].keys():
            if neighbor not in visited:
                self.dfs(neighbor, visited, stack)
        stack.append(node) # add node to stack since it cannot be explored further
    

def main():
    graph = {
        'a': {'b': 2, 'e': 2},
        'b': {'c': 2},
        'c': {'t': 4},
        'd': {'a': 3, 'e': 3},
        'e': {'c': 2, 'f': 3, 'i': 3},
        'f': {'c': 1, 't': 3},
        'g': {'d': 2, 'e': 1, 'h': 6},
        'h': {'e': 2, 'i': 6},
        'i': {'f': 1, 't': 4},
        's': {'a': 1, 'd': 4, 'g': 6},
        't': {}
    }
    
    g = Graph(graph)
    topSort = g.topSort()
    print()
    print(f"topological sort of nodes: {topSort}")
    print()
    

if __name__ == '__main__':
    main()

