
print()

import networkx
from networkx import algorithms
import matplotlib

# create a weighted graph
G = networkx.Graph()
nA, nB, nC, nD, nE = 'A', 'B', 'C', 'D', 'E'
G.add_nodes_from([nA, nB, nC, nD, nE])
G.add_weighted_edges_from([(nA,nB,2),(nB,nC,3),(nC,nD,4)])
G.add_weighted_edges_from([(nA,nE,9),(nE,nD,10)])

# Graph Distance:
#    Unweighted distance - number of edges between two nodes
#    Weighted distance - sum of weights between two nodes. 
#        so shortest path is least combined weight, not necessarily the fewest nodes

# Dijkstra's Algorithm:
#    For a given vertex it finds the lowest cost path to all other vertices, 
#    where “cost” is determined by summing edge weights. In graphs where edge 
#    weights correspond to distance (in unweighted graphs the weights are 
#    assumed to be one) the found path is the shortest. 
#    The algorithm can also determine the lowest cost path between two given 
#    vertices.

print ("Shortest Path from node A to node D:")
print (algorithms.shortest_path(G,nA,nD))
print ()

print ("Dijkstra Shortest Path from node A to node D:")
print (algorithms.dijkstra_path(G,nA,nD))

# plot the weighted graph
pos=networkx.spring_layout(G)
matplotlib.pyplot.figure(figsize=(10,10))
networkx.draw_networkx_nodes(G,pos,node_size=1500)
networkx.draw_networkx_labels(G,pos,font_size=20)
edgewidth = [ d['weight'] for (u,v,d) in G.edges(data=True)]
networkx.draw_networkx_edges(G,pos,edge_color=edgewidth,width=edgewidth)
edgelabel = networkx.get_edge_attributes(G,'weight')
networkx.draw_networkx_edge_labels(G,pos,edge_labels=edgelabel,font_size=20)
matplotlib.pyplot.axis('off')
#matplotlib.pyplot.savefig("graph.png") 
matplotlib.pyplot.show()