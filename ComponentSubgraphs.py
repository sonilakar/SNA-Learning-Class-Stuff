

print ()

# Component Subgraph (or simply Component): 
#     portions of the network that are disconnected from each other. 

import networkx
import matplotlib

# create a graph with two components for illustration
G = networkx.Graph()
nA, nB, nC, nD, nE, nF, nG, nH, nI, nJ = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'
G.add_nodes_from([nA, nB, nC, nD, nE, nF, nG, nH, nI, nJ])
G.add_edges_from([(nA,nB),(nA,nC),(nC,nD),(nA,nD),(nD,nE),(nF,nG),(nF,nH),(nF,nI),(nH,nJ)])

# define subgraphs for the two components
comp1 = G.subgraph(['A', 'B', 'C', 'D', 'E']) 
comp2 = G.subgraph(['F', 'G', 'H', 'I', 'J'])

# plot the graph and the components
pos = networkx.spring_layout(G)  
matplotlib.pyplot.figure(figsize=(10,10))
networkx.draw_networkx_labels(G,pos,font_size=20)
networkx.draw(G, pos=pos, node_size=1500, node_color='r', edge_color='r', style='solid')
networkx.draw(comp1, pos=pos, node_size=1000, node_color='b', edge_color='b', style='solid')
networkx.draw(comp2, pos=pos, node_size=1000, node_color='g', edge_color='g', style='solid')
matplotlib.pyplot.show()