#model
def cerca_cammino_minimo(self, partenza):
    self.best_cammino = []
    self.best_peso = float('inf')

    parziale = [partenza]
    self._ricorsione_min(parziale, 0, float('-inf'))  # peso precedente inizializzato a -∞

    return self.best_cammino, self.best_peso


def _ricorsione_min(self, parziale, peso_attuale, peso_precedente):
    ultimo = parziale[-1]

    for vicino in self._graph.successors(ultimo):
        if vicino in parziale:
            continue

        peso = self._graph[ultimo][vicino]['weight']

        if peso > peso_precedente:  # STRETTAMENTE crescente
            parziale.append(vicino)
            self._ricorsione_min(parziale, peso_attuale + peso, peso)
            parziale.pop()

    if len(parziale) > 1 and peso_attuale < self.best_peso:
        self.best_peso = peso_attuale
        self.best_cammino = list(parziale)
#controller
def handle_cammino_minimo(self, e):
    nodo_partenza = self._view.get_selected_node()
    if nodo_partenza is None:
        self._view.show_message("Seleziona un nodo di partenza")
        return

    cammino, peso = self._model.cerca_cammino_minimo(nodo_partenza)
    self._view.mostra_risultato_minimo(cammino, peso)
