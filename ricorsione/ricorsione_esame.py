def cerca_percorso(self, nodo_corrente, nodo_target, lunghezza_attuale, percorso, visited):
    if lunghezza_attuale == self.lunghezza_target:
        if nodo_corrente == nodo_target:
            self.percorsi_validi.append(list(percorso))
        return

    for vicino in self._graph.neighbors(nodo_corrente):
        if vicino not in visited:
            peso = self._graph[nodo_corrente][vicino]['peso']  # opzionale
            percorso.append(vicino)
            visited.add(vicino)
            self.cerca_percorso(vicino, nodo_target, lunghezza_attuale + 1, percorso, visited)
            visited.remove(vicino)
            percorso.pop()

def handleRicercaPercorso(self, e):
    start = self._view.ddStart.value
    end = self._view.ddEnd.value
    self.lunghezza_target = int(self._view.txtLunghezza.value)

    self.percorsi_validi = []

    percorso = [start]
    visited = set([start])

    self.cerca_percorso(start, end, 0, percorso, visited)

    # Mostra i risultati
    if self.percorsi_validi:
        self._view.txt_result.controls.append(ft.Text(f"Trovati {len(self.percorsi_validi)} percorsi:"))
        for p in self.percorsi_validi:
            self._view.txt_result.controls.append(ft.Text(" → ".join(str(n) for n in p)))
    else:
        self._view.txt_result.controls.append(ft.Text("Nessun percorso trovato."))

    self._view._page.update()
# controller
#per il view
# self._view.ddStart.options = [ft.dropdown.Option(str(n)) for n in self._graph.nodes]
# self._view.ddEnd.options = [ft.dropdown.Option(str(n)) for n in self._graph.nodes]
