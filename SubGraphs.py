
print ()

# Subgraph: 
#     subset of nodes in a network, along with all of the edges linking these nodes. 

import networkx 
import matplotlib  

# use the kite graph
G = networkx.generators.small.krackhardt_kite_graph()

# define a subgraph with nodes 0, 1, 2, 3, 4, 5
subgraph = G.subgraph([0,1,2,3,4,5]) 

# plot the graph and subgraph
pos = networkx.spring_layout(G)  
matplotlib.pyplot.figure(figsize=(10,10))
networkx.draw_networkx_labels(G,pos,font_size=20)
networkx.draw(G, pos=pos, node_size=1500, node_color='r', edge_color='r', style='dashed')
networkx.draw(subgraph, pos=pos, node_size=1000, node_color='g', edge_color='g', style='solid')
matplotlib.pyplot.show()