import numpy as np
import networkx as nx

# Define the number of nodes
N = 9

# Define adjacency matrix with given weighted edges
adj_matrix = np.zeros((N, N), dtype = int)

edges = [
    (1,2,4), (1,4,2), (2,3,3), (2,6,4),
    (3,7,14), (4,5,8), (5,6,5), (5,9,10),
    (5,5,9), (6,7,7), (7,3,12), (7,8,13),
    (8,9,15)
]

# Populate adjacency matrix
for u, v, w in edges:
    adj_matrix[u-1][v-1] = w #Convert 1-based index to 0-based
    
# Print adjacency matrix
print("Adjacency Matrix: ")
print(adj_matrix)

# Create a directed graph using networkx
G = nx.DiGraph()
G.add_weighted_edges_from(edges)

# Find weakly connected components
G_undirected = G.to_undirected() # Conver to undirected graph
num_wcc = nx.number_connected_components(G_undirected)

# Find strongly connected components
scc = list(nx.strongly_connected_components(G))
num_scc = len(scc)

# Print results
print(f"Number of weakly connected components is: {num_wcc}")
print(f"Number of strongly connected components is: {num_scc}")

# Print SCCs
print("Strongly connected components: ")
for i, component in enumerate(scc, 1):
    print(f"SCC {i}: {component}")
