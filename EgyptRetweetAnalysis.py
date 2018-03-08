

print ()

# twitter data and code adapted from here:
# https://github.com/maksim2042/SNABook

# Twitter retweet network:
#     Twitter users are nodes; retweets are links between nodes
#     over time people tend to retweet from those they trust
#     So over time a twitter retweet network is a proxy for trust networks

import networkx
import networkx.generators.small

# load Egyptian Revolution Retweet Data
# https://en.wikipedia.org/wiki/Wael_Ghonim
G=networkx.read_pajek(".\data\egypt_retweets.net")

print ("Number of Nodes:")
print (G.number_of_nodes())
print ()

print ("Number of Edges:")
print (G.number_of_edges())
print ()

# Components
print ("Number of Component Subgraphs:")
print (len(list(networkx.connected_component_subgraphs(G))))
print ()

print ("Number of Nodes in Component Subgraphs with > 10 Nodes:")
x=[len(c) for c in networkx.connected_component_subgraphs(G) if len(c) > 10]
print (x)
print ()

# Islands
def trim_edges(g, threshold=1):
    gtmp = networkx.Graph()
    for f, to, edata in g.edges(data=True):
        if edata['weight'] > threshold:
            gtmp.add_edge(f,to,edata)
    return gtmp

print ('Threshold', 'Nodes', 'Islands')
for threshold in range(0,25):
    g = trim_edges(G, threshold)
    print (threshold, g.number_of_nodes(), len(list(networkx.connected_component_subgraphs(g))))
print ()

# Egos
ben = networkx.Graph(networkx.ego_graph(G, 'justinbieber', radius=3))
gen = networkx.Graph(networkx.ego_graph(G, 'Ghonim', radius=3))
print ('Ego(r=3)', 'Nodes', 'Edges')
print ('Beiber', ben.number_of_nodes(), ben.number_of_edges())
print ('Ghonim', gen.number_of_nodes(), gen.number_of_edges())
print ()

# Clustering Coefficient
ben = networkx.Graph(networkx.ego_graph(G, 'justinbieber', radius=1))
gen = networkx.Graph(networkx.ego_graph(G, 'Ghonim', radius=1))
print ('Ego(r=1)', 'Nodes', 'Edges', 'ClusCoeff')
print ('Beiber', ben.number_of_nodes(), ben.number_of_edges(), round(networkx.average_clustering(ben),2))
print ('Ghonim', gen.number_of_nodes(), gen.number_of_edges(), round(networkx.average_clustering(gen),2))
print ()

