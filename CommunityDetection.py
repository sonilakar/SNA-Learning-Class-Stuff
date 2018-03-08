

# references:
#     algorithm: https://perso.uclouvain.be/vincent.blondel/research/louvain.html
#     module:    http://perso.crans.org/aynaud/communities/
#     code:      https://app.dominodatalab.com/LeJit/FacebookNetwork/browse?
#     snap data: https://snap.stanford.edu/data/

import networkx
import matplotlib.pyplot

import sys
sys.path.insert(0,"C:\\Users\\hina\\Anaconda3\\Lib\\site-packages\\python_louvain-0.4-py3.6.egg")
import community
 
# get data
#G = networkx.karate_club_graph()
G = networkx.read_edgelist("data/facebook_combined.txt", create_using = networkx.Graph(), nodetype = int)

# get general stats of network
print (networkx.info(G))

# generate communities
parts = community.best_partition(G)
values = [parts.get(node) for node in G.nodes()]

# show communities
pos = networkx.spring_layout(G)
matplotlib.pyplot.figure(figsize=(20,20))
matplotlib.pyplot.axis("off")
networkx.draw_networkx(G, pos=pos, cmap=matplotlib.pyplot.get_cmap("hsv"), node_color=values, node_size=100, with_labels=False)
matplotlib.pyplot.savefig("communityDetection.png") 
matplotlib.pyplot.show()

