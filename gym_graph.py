import networkx as nx
import matplotlib.pyplot as plt

# Define the gym locations (nodes) and their coordinates
gym_locations = {
    'Gym A': (28.6139, 77.2090),  # Example coordinates
    'Gym B': (28.7041, 77.1025),
    'Gym C': (28.5355, 77.3910),
    'Gym D': (28.4595, 77.0266),
    'Gym E': (28.4089, 77.3178)
}

# Create a graph
G = nx.Graph()

# Add nodes with positions
for gym, pos in gym_locations.items():
    G.add_node(gym, pos=pos)

# Define connections (edges) between gyms
edges = [
    ('Gym A', 'Gym B'),
    ('Gym B', 'Gym C'),
    ('Gym C', 'Gym D'),
    ('Gym D', 'Gym E'),
    ('Gym E', 'Gym A')
]

# Add edges to the graph
G.add_edges_from(edges)

# Get positions for all nodes
pos = nx.get_node_attributes(G, 'pos')

# Draw the graph and save it as an image
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
plt.title('Gym Locations and Connections')
plt.savefig('app/static/images/gym_graph.png')
plt.close()
