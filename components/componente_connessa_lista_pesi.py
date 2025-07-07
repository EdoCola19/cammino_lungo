# componenti = list(nx.connected_components(self._model._graph))
#         componente_max = max(componenti, key=len)
#         sottografo = self._model._graph.subgraph(componente_max)
#         pesi_per_nodo = {}
#         for nodo in sottografo.nodes:
#             pesi = []
#             for _,_,d in sottografo.edges(nodo, data=True):
#                 pesi.append(d["peso"])
#             peso_min = min(pesi) if pesi else 0
#             pesi_per_nodo[nodo] = peso_min
#
#
#         nodi_ordinati = sorted(pesi_per_nodo.items(), key= lambda x:x[1], reverse=True)
#         self._view._txtGraphDetails.controls.append(ft.Text(f"Stampa dettagli:"))
#         for nodo, peso in nodi_ordinati:
#             self._view._txtGraphDetails.controls.append(ft.Text(f"{nodo.name} -- {peso}"))
#         self._view._page.update()
#grafo non orientato ma pesato, se fosse orientato avrei usato weakly_connected
