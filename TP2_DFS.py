from collections import deque  # Import deque for BFS queue

# Define the graph using an adjacency list
edges = [
    (1, 2), (1, 4), (2, 3), (2, 6), (3, 7), (3, 8), 
    (4, 5), (5, 6), (5, 9), (6, 7), (7, 5), (7, 8), (8, 9)
]

# Determine the number of nodes (find max node label)
N = max(max(u, v) for u, v in edges)

# Create an adjacency list representation of the graph
graph = {i: [] for i in range(1, N + 1)}  # Create empty adjacency list

for u, v in edges:
    graph[u].append(v)  # Add edge (directed graph)

# Implement DFS
def dfs(start_node, visited=None):
    """Performs Depth-First Search (DFS) starting from start_node."""
    if visited is None:
        visited = set()  # Keep track of visited nodes

    print(start_node, end=" ")  # Print node
    visited.add(start_node)  # Mark as visited
    
    for neighbor in graph[start_node]:  # Explore each neighbor
        if neighbor not in visited:
            dfs(neighbor, visited)  # Recursive call

# Running and DFS
start_node = 1  # Start traversal from node 1
print("Graph Representation (Adjacency List):")
for node in graph:
    print(f"{node}: {graph[node]}")  # Print adjacency list

print("\nDepth-First Search (DFS) starting from node", start_node)
dfs(start_node)

print()  # Newline for formatting
