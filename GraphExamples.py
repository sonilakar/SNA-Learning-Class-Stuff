# code adapted from here:
# https://github.com/maksim2042/SNABook

print()

import networkx
import networkx.generators.small
import matplotlib.pyplot

#G = networkx.generators.small.bull_graph()
#G = networkx.generators.complete_graph(4)
#G = networkx.generators.diamond_graph()
G = networkx.generators.small.krackhardt_kite_graph()
#G = networkx.karate_club_graph()

# plot the graph
pos=networkx.spring_layout(G)
matplotlib.pyplot.figure(figsize=(15,15))
networkx.draw_networkx_nodes(G,pos,node_size=600)
networkx.draw_networkx_labels(G,pos,font_size=18)
networkx.draw_networkx_edges(G,pos)
matplotlib.pyplot.axis('off')
#matplotlib.pyplot.savefig("graph.png") 
matplotlib.pyplot.show()

