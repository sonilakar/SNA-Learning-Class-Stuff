# code adapted from here:
# https://github.com/maksim2042/SNABook

# Social Networks are graphs.
# A graph is a collection of Nodes and Edges.
# Edges can be Directed, and can have Weight.

print()

import matplotlib.pyplot
import networkx
import networkx.generators.small

#G = networkx.generators.small.bull_graph()
# G = networkx.generators.diamond_graph()
G = networkx.generators.small.krackhardt_kite_graph()
# G = networkx.karate_club_graph()

# plot the graph
pos=networkx.spring_layout(G)
networkx.draw_networkx_nodes(G,pos, node_size = 600)
networkx.draw_networkx_labels(G,pos, font_size=18)
networkx.draw_networkx_edges(G,pos)
matplotlib.pyplot.axis('off')
#matplotlib.pyplot.savefig("graph.png") 
matplotlib.pyplot.show() 

adjacencyList = G.adjacency_list()

# Degree Centrality (celebrities): 
#     number of connections that a node has
degreeCentrality = networkx.degree(G)
#print (degreeCentrality)

# Closeness Centrality (gossipmongers):
#     compute shortest path between every pair of nodes using Dijkstra’s algorithm
#     then for every node:
#         compute average (shortest) distance to all other nodes
#         divide by maximum distance (normalizes to 0-1 range)
#         closeness = 1 divided by average distance 
closenessCentrality = networkx.closeness_centrality(G)
#print (closenessCentrality)

# Betweenness Centrality (bottlenecks or bridges or boundary spanners):
#    compute shortest paths between every pair of nodes using Dijkstra's algorithm
#    then for every node:
#        count the number of shortest paths that node is on
#        divide by maximum numer of shortest paths (normalizes to 0-1 range)
betweennessCentrality = networkx.betweenness_centrality(G)
#print (betweennessCentrality)

# Eigenvector Centrality (grey cardinals - powerful but behind the scenes):
#    recursive version of degree centrality... node high on eigenvector centrality 
#    is essentially connected to many high degree nodes
eigenvectorCentrality = networkx.eigenvector_centrality(G)
#print (eigenvectorCentrality)

printFormat = "{0:<5} {1:<7} {2:<10} {3:<12} {4:<12} {5}"
print(printFormat.format('Node', 'Degree', 'Closeness', 'Betweenness', 'Eigenvector', 'Adjacency'))
for n in networkx.nodes(G):
    print(printFormat.format(n, round(degreeCentrality[n],2), round(closenessCentrality[n],2), round(betweennessCentrality[n],2), round(eigenvectorCentrality[n],2), adjacencyList[n]))




