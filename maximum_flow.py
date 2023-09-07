# Graphs: Maximum Flow and Ford Fulkerson Implementation

class Graph(object):
    
    # initialize graphs
    def __init__(self, graph):
        self.graph = graph
        self.residual = self.createResidualGraph()
        self.flow = self.createFlowGraph()
    
    # create flow graph
    def createFlowGraph(self):
        flowGraph = {}
        for node in self.graph:
            flowGraph[node] = {}
            for neighbor in self.graph[node]:
                flowGraph[node][neighbor] = 0
        return flowGraph
    
    # create residual graph
    def createResidualGraph(self):
        residualGraph = {}
        
        # copy original graph to residual graph
        for node in self.graph:
            residualGraph[node] = {}
            for neighbor in self.graph[node]:
                residualGraph[node][neighbor] = self.graph[node][neighbor]
        
        # add backward edges
        for node in self.graph:
            for neighbor in self.graph[node]:
                if node not in residualGraph[neighbor]:
                    residualGraph[neighbor][node] = 0 # backward edges have cap of 0

        return residualGraph
    
    # find augmented path using bfs
    # returns dict where key = node and value = (parent node, capacity of edge from parent to node)
    def findAugmentedPath(self, source, sink):
        # intialize queue with source node and capacity
        queue = [(source, float('inf'))]
        # track visited nodes and node we arrived from (parent), along with capacity of edge from parent
        visited = {source: (None, float('inf'))}  
        
        while queue:
            curr, capacity = queue.pop(0) # dequeue current node and capacity
            for neighbor in self.residual[curr]:
                residualCapacity = self.residual[curr][neighbor]
                # only visit nodes that haven't already been visited and are viable options for augmented path (resid cap > 0)
                if neighbor not in visited and residualCapacity > 0:
                    visited[neighbor] = (curr, min(capacity, residualCapacity)) # record parent and capacity of edge to neighbor 
                    if neighbor == sink: # found path
                        #print(visited)
                        return visited
                    queue.append((neighbor, min(capacity, residualCapacity))) # enqueue neighbor
        
        return None # no path found
    
    # finds bottleneck capacity of an augmented path
    def bottleneckCapacity(self, source, sink, parentDict):
        node = sink 
        bottleneckCapacity = float('inf') 
        while node != source:
            prevNode, capacity = parentDict[node]
            bottleneckCapacity = min(bottleneckCapacity, capacity)
            node = prevNode
        return bottleneckCapacity
    
    # updates flow and residual graphs using bottleneck capacity and augmented path
    def updateFlowAndResidual(self, source, sink, parentDict):
        bottleneck = self.bottleneckCapacity(source, sink, parentDict)
        
        node = sink
        while node != source:
            prevNode = parentDict[node][0] # where we arrived from
            
            # update flow graph
            self.flow[prevNode][node] += bottleneck
            
            # update residual graph
            self.residual[prevNode][node] -= bottleneck # reduce capacity of forward edges
            self.residual[node][prevNode] += bottleneck # increase capacity of backward edges (i.e. flow that could be undone)
            
            node = prevNode
    
    # helper function used for printing augmented path
    def getPath(self, sink, parentDict):
        path = []
        node = sink
        while node is not None:
            path.append(node)
            node = parentDict[node][0]
        path.reverse()
        return path

    # driver method for implementing ford-fulkerson algorithm
    def findMaxFlow(self, source, sink):
        print("Augmented paths:")
        
        while True:
            parentDict = self.findAugmentedPath(source, sink)
            if parentDict is None:
                break
            
            # prints path with flow
            path = self.getPath(sink, parentDict)
            bottleneck = self.bottleneckCapacity(source, sink, parentDict)
            path.append({'flow': bottleneck})
            print(path)
            
            self.updateFlowAndResidual(source, sink, parentDict)
        
        # max flow is sum of values outbound from source after updations are complete
        return sum(self.flow[source].values())

def main():
    
    originalGraph = {
       's': {'a': 4, 'b': 2},
       'a': {'b': 1, 'c': 2, 'd': 4},
       'b': {'d': 2},
       'c': {'t': 3},
       'd': {'t': 3},
       't': {} 
    }
    
    print()
    g = Graph(originalGraph)
    maxFlow = g.findMaxFlow('s', 't')
    print()
    print(f"Maximum flow: {maxFlow}")
    print()
    
if __name__ == '__main__':
    main()