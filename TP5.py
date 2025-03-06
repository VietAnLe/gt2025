import sys

def dijkstra(graph, start, end):
    n = len(graph)
    distances = [sys.maxsize] * n  # Initialize all distances to infinity
    previous = [-1] * n            # Store previous nodes for path reconstruction
    visited = [False] * n          # Track visited nodes

    distances[start] = 0  # Distance from start to itself is 0

    while True:
        # Find the closest unvisited node
        min_node = -1
        min_dist = sys.maxsize
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                min_node = i

        if min_node == -1:  # If no reachable nodes remain, stop
            break

        visited[min_node] = True

        # Update distances to neighboring nodes
        for neighbor, weight in enumerate(graph[min_node]):
            if weight != float('inf') and not visited[neighbor]:
                new_dist = distances[min_node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = min_node

    # Reconstruct the shortest path
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = previous[current]

    path.reverse()  # Reverse to get the correct order

    return path, distances[end]

# Define graph as an adjacency matrix
graph = [
    [0, 4, 1, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [4, 0, float('inf'), float('inf'), float('inf'), 3, float('inf'), float('inf'), float('inf'), float('inf')],
    [1, float('inf'), 0, 8, float('inf'), 7, float('inf'), float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), 8, 0, float('inf'), float('inf'), float('inf'), 5, float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0, 1, float('inf'), 2, 2, float('inf')],
    [float('inf'), 3, 7, float('inf'), 1, 0, float('inf'), 1, float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0, 3, 4, 4],
    [float('inf'), float('inf'), float('inf'), 5, 2, 1, 3, 0, 6, 7],
    [float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'), 4, 6, 0, 1],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 4, 7, 1, 0]
]

# Node labels
nodes = "ABCDEFGHLM"

# Get user input
start_label = input("Enter start node (A-M): ").strip().upper()
end_label = input("Enter end node (A-M): ").strip().upper()

start = nodes.index(start_label)
end = nodes.index(end_label)

# Run Dijkstra's algorithm
path, total_distance = dijkstra(graph, start, end)

# Convert path indices to node labels
path_labels = [nodes[i] for i in path]

# Output results
print("Shortest Path:", " → ".join(path_labels))
print("Total Distance:", total_distance)
