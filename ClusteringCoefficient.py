
print ()

# Clustering Coefficient:
#     measures the proportion of teh ego's friends that are also friends with each other  
#     star networks with a single broadcast node and passive listeners have a low clustering coefficient.
#     dense ego networks with a lot of mutual trust have a high clustering coefficient.

import matplotlib.pyplot
import networkx

# use the karate club graph
G = networkx.karate_club_graph()

# get ego network of node n at depth 1
n = 32
ego = networkx.ego_graph(G, n, radius=1)

# get the clustering coefficient of the ego network
print (n, round (networkx.average_clustering(ego),2))

# plot the graph and the ego network
pos = networkx.spring_layout(G)  
matplotlib.pyplot.figure(figsize=(10,10))
networkx.draw_networkx_labels(G,pos,font_size=20)
networkx.draw(G, pos=pos, node_size=1500, node_color='r', edge_color='r', style='dashed')
networkx.draw(ego, pos=pos, node_size=1000, node_color='b', edge_color='b', style='solid')
matplotlib.pyplot.show()