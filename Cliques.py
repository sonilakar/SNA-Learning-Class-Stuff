

import matplotlib.pyplot
import networkx

# use the karate club graph
G = networkx.karate_club_graph()

# list the cliques
print(list(networkx.find_cliques(G)))

# create a subgraph with the largest clique (as found in list above)
clique = G.subgraph([0, 1, 2, 3, 13]) 

print (clique.number_of_nodes())

# plot the graph and the largest clique
pos = networkx.spring_layout(G)
matplotlib.pyplot.figure(figsize=(10,10))
networkx.draw_networkx_labels(G,pos,font_size=20)
networkx.draw(G, pos=pos, node_size=1500, node_color='r', edge_color='r', style='dashed')
networkx.draw(clique, pos=pos, node_size=1000, node_color='b', edge_color='b', style='solid')
matplotlib.pyplot.show()