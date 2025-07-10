#model
def cerca_cammino_massimo(self, partenza):
    self.best_cammino = []
    self.best_peso = 0

    parziale = [partenza]
    self._ricorsione(parziale, 0, float('inf'))  # peso precedente inizializzato a infinito

    return self.best_cammino, self.best_peso


def _ricorsione(self, parziale, peso_attuale, peso_precedente):
    ultimo = parziale[-1]

    for vicino in self._graph.successors(ultimo):
        if vicino in parziale:
            continue

        peso = self._graph[ultimo][vicino]['weight']

        if peso < peso_precedente:
            parziale.append(vicino)
            self._ricorsione(parziale, peso_attuale + peso, peso)
            parziale.pop()

    if peso_attuale > self.best_peso:
        self.best_peso = peso_attuale
        self.best_cammino = list(parziale)
#controller
def handle_ricorsione(self, e):
    nodo_partenza = self._view.get_selected_node()  # oppure prendi il nodo dal dropdown
    if nodo_partenza is None:
        self._view.show_message("Seleziona un nodo di partenza")
        return

    cammino, peso = self._model.cerca_cammino_massimo(nodo_partenza)

    self._view.mostra_risultato_ricorsione(cammino, peso)
