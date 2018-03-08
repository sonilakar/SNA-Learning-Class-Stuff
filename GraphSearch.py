# code adapted from here:
# https://github.com/maksim2042/SNABook

# We often want to be able to traverse the structure of a graph or network
#     to find the shortest path from node A to node B, or to understand the 
#     structure of the graph. 

print()

import matplotlib.pyplot
import networkx
from networkx import algorithms
from networkx import generators

G = generators.small.bull_graph()
#G = networkx.generators.diamond_graph()
#G = networkx.generators.small.krackhardt_kite_graph()
#G = networkx.karate_club_graph()

# Depth First Search:
#     Go deep before going broad.
#     visit the neighbor's neighbors first and
#     only then proceed to the neighbors
print ("Depth First Search")
print (list(algorithms.traversal.dfs_edges(G, 0)))
print ()

# Breadth First Search:
#     visit all of the immediate neighbors first and 
#     only then proceeds to their neighbors.
print ("Breadth First Search")
print (list(algorithms.traversal.bfs_edges(G, 0)))
print ()

# plot the graph
pos=networkx.spring_layout(G)
networkx.draw_networkx_nodes(G,pos)
networkx.draw_networkx_edges(G,pos)
networkx.draw_networkx_labels(G,pos)
matplotlib.pyplot.axis('off')
#matplotlib.pyplot.savefig("graph.png") 
matplotlib.pyplot.show() 