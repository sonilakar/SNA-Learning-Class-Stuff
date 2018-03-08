
print ()

# twitter data and code adapted from here:
# https://github.com/maksim2042/SNABook

# Islands:
#     Only retain edges (and correspodning from/to nodes) 
#       if edge weight > threshold
#       (ex: only retain edges if edge weight > 25 retweets).
#     what remains is subcores of maximal activity between nodes that have 
#         developed a trust relationship.

import matplotlib.pyplot
import networkx
import networkx.generators.small
from networkx import generators

# create a weighted graph
G = networkx.Graph()
nA, nB, nC, nD, nE, nF = 'A', 'B', 'C', 'D', 'E', 'F'
G.add_nodes_from([nA, nB, nC, nD, nE, nF])
G.add_weighted_edges_from([(nA,nB,2)])
G.add_weighted_edges_from([(nA,nE,9)])
G.add_weighted_edges_from([(nA,nF,6)])
G.add_weighted_edges_from([(nB,nC,3)])
G.add_weighted_edges_from([(nC,nD,7)])
G.add_weighted_edges_from([(nD,nE,3)])
G.add_weighted_edges_from([(nE,nF,10)])

# plot the weighted graph
pos=networkx.spring_layout(G)
matplotlib.pyplot.figure(figsize=(10,10))
networkx.draw_networkx_nodes(G,pos,node_size=1500)
networkx.draw_networkx_labels(G,pos,font_size=20)
edgewidth = [ d['weight'] for (u,v,d) in G.edges(data=True)]
networkx.draw_networkx_edges(G,pos,width=edgewidth)
edgelabel = networkx.get_edge_attributes(G,'weight')
networkx.draw_networkx_edge_labels(G,pos,edge_labels=edgelabel,font_size=20)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.show()

# Use island method:
# Only retain edges (and corresponding from/to nodes) 
# if edge weight > threshold
threshold= 5
gIslands = networkx.Graph()
for f, t, e in G.edges(data=True):
    if e['weight'] > threshold:
        gIslands.add_edge(f,t,e)

# plot the resulting graphs with resulting islands
pos=networkx.spring_layout(gIslands)
matplotlib.pyplot.figure(figsize=(10,10))
networkx.draw_networkx_nodes(gIslands,pos,node_size=1500)
networkx.draw_networkx_labels(gIslands,pos,font_size=20)
edgewidth = [ d['weight'] for (u,v,d) in gIslands.edges(data=True)]
networkx.draw_networkx_edges(gIslands,pos,width=edgewidth)
edgelabel = networkx.get_edge_attributes(gIslands,'weight')
networkx.draw_networkx_edge_labels(gIslands,pos,edge_labels=edgelabel,font_size=20)
matplotlib.pyplot.axis('off') 
matplotlib.pyplot.show()