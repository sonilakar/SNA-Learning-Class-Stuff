

print ()

# Ego Networks:
#     Subnetworks that are centered on a certain node.
#     Derived by running a breath-first search, and limiting depth to <= 3.
#         intuitivel this is becuase, we know our friends quite well, 
#         our friends’ friends somewhat well, 
#         and our friends’ friends’ friends almost not at all.

import matplotlib.pyplot
import networkx

# use the karate club graph
G = networkx.karate_club_graph()

# define the ego network for node n at depth 1
n = 1000
ego = networkx.ego_graph(G, n, radius=1)
#print (G.neighbors(n))

# plot the graph and the ego network
pos = networkx.spring_layout(G)  
matplotlib.pyplot.figure(figsize=(5,5))
networkx.draw_networkx_labels(G,pos,font_size=5)
networkx.draw(G, pos=pos, node_size=500, node_color='r', edge_color='r', style='dashed')
networkx.draw(ego, pos=pos, node_size=250, node_color='b', edge_color='b', style='solid')
matplotlib.pyplot.show()