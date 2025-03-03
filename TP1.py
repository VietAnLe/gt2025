class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def path_exist(self, start, end, visited=None):
        if visited is None:
            visited = set()
            
        if start == end:
            return True
        
        visited.add(start)
        
        for neighbor in self.adj_list.get(start, []):
            if neighbor not in visited:
                if self.path_exist(neighbor, end, visited):
                    return True
                
            return False
        
# Create graph instance
graph = Graph()

# Adding edges based
graph.add_edge(1, 2)
graph.add_edge(1, 5)
graph.add_edge(3, 6)
graph.add_edge(4, 6)
graph.add_edge(4, 7)
graph.add_edge(6, 7)

# Taking user input for the node paris
start_node = int(input("Enter start node: "))
end_node = int(input("Enter end node: "))

# Checking if a path exists
print("True" if graph.path_exist(start_node, end_node) else "False")
