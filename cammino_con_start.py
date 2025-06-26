import networkx as nx

def cammino_piu_lungo_da_nodo(grafo, start):
    if not nx.is_directed_acyclic_graph(grafo):
        print("Il grafo contiene cicli, il calcolo del cammino più lungo non è supportato in questo caso.")
        return None

    # Dizionario delle lunghezze massime a partire da 'start'
    memo = {}
    percorso_migliore = []

    def dfs(nodo, percorso_corrente):
        nonlocal percorso_migliore

        # Salva il miglior cammino trovato finora
        if len(percorso_corrente) > len(percorso_migliore):
            percorso_migliore = list(percorso_corrente)

        for vicino in grafo.successors(nodo):
            if vicino not in percorso_corrente:  # Evita cicli
                dfs(vicino, percorso_corrente + [vicino])

    # Avvia DFS dal nodo selezionato
    dfs(start, [start])

    return percorso_migliore

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

nodo_selezionato = 'A'  # Simula la selezione dal menu a tendina
cammino = cammino_piu_lungo_da_nodo(G, nodo_selezionato)
print("Cammino più lungo da", nodo_selezionato, ":", cammino)
