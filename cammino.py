import networkx as nx

def cammino_piu_lungo_dag(grafo):
    try:
        # Controlla se è aciclico
        if not nx.is_directed_acyclic_graph(grafo):
            print("Il grafo contiene cicli, il calcolo del cammino più lungo non è supportato in questo caso.")
            return None

        # Calcola tutti i cammini più lunghi tra le coppie di nodi
        lunghezze = {}
        predecessori = {}
        for nodo in nx.topological_sort(grafo):
            lunghezza_max = 0
            predecessore = None
            for pred in grafo.predecessors(nodo):
                lunghezza = lunghezze[pred] + 1
                if lunghezza > lunghezza_max:
                    lunghezza_max = lunghezza
                    predecessore = pred
            lunghezze[nodo] = lunghezza_max
            predecessori[nodo] = predecessore

        # Trova il nodo con il cammino più lungo
        ultimo_nodo = max(lunghezze, key=lunghezze.get)
        cammino = []
        while ultimo_nodo is not None:
            cammino.insert(0, ultimo_nodo)
            ultimo_nodo = predecessori[ultimo_nodo]

        return cammino

    except Exception as e:
        print(f"Errore durante il calcolo: {e}")
        return None


# === ESEMPIO DI UTILIZZO ===

G = nx.DiGraph()
G.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('D', 'E'),
    ('E', 'F')
])

cammino = cammino_piu_lungo_dag(G)
print("Cammino più lungo:", cammino)
