import networkx as nx
import graphviz 

G = nx.Graph() # crear un grafo

#Añadir nodos
G.add_node("A")
G.add_node("B")
G.add_nodes_from(["C", "D", "F"])

#Añadir aristas
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edges_from([("B", "C"), ("B", "D")])
G.add_edges_from([("D", "C"), ("D", "F")])

print(len(G.nodes))
print(len(G.edges))
print(G.nodes)
print(G.edges)

# A = nx.nx_agraph.to_agraph(G)
# A.layout('dot')
# graphviz.Source(A.to_string())
