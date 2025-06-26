#controller
def handle_dettagli_squadra(self, e):
    squadra_selezionata = self._view.ddsquadra.value
    if squadra_selezionata is None:
        self._view.txtResult.value = "Seleziona una squadra."
        self._view.update()
        return

    adiacenti = self._model.get_adiacenti(squadra_selezionata)

    if not adiacenti:
        self._view.txtResult.value = "Nessuna squadra adiacente trovata."
    else:
        result = f"Squadre adiacenti a {squadra_selezionata}:\n"
        for squadra, peso in adiacenti:
            result += f"- {squadra}: peso = {peso}\n"
        self._view.txtResult.value = result

    self._view.update()
#model
import networkx as nx

class Model:
    def __init__(self):
        self._graph = nx.Graph()  # o nx.DiGraph() se orientato

    def get_adiacenti(self, squadra):
        if squadra not in self._graph:
            return []

        adiacenti = []
        for vicino in self._graph.neighbors(squadra):
            peso = self._graph[squadra][vicino]['weight']
            adiacenti.append((vicino, peso))

        # Ordinamento decrescente per peso
        adiacenti.sort(key=lambda x: x[1], reverse=True)
        return adiacenti
