import networkx as nx

# Creazione del grafo (puoi usare DiGraph() per un grafo orientato)
G = nx.Graph()

# Aggiunta dei nodi (facoltativa, se aggiunti automaticamente con gli archi)
G.add_nodes_from(["A", "B", "C", "D", "E"])

# Aggiunta degli archi con pesi
G.add_edge("A", "B", weight=1)
G.add_edge("B", "C", weight=2)
G.add_edge("A", "D", weight=4)
G.add_edge("D", "E", weight=1)
G.add_edge("E", "C", weight=1)

# Nodo di partenza e di arrivo
start = "A"
end = "C"

# Calcolo del cammino più breve
try:
    path = nx.dijkstra_path(G, source=start, target=end, weight='weight')
    length = nx.dijkstra_path_length(G, source=start, target=end, weight='weight')

    print(f"Cammino più breve da {start} a {end}: {path}")
    print(f"Lunghezza del cammino: {length}")
except nx.NetworkXNoPath:
    print(f"Nessun cammino disponibile da {start} a {end}.")
