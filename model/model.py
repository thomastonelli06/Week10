import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._lista_luoghi = None
        self.dizionario_luoghi = {}
        self.grafo = nx.Graph() #creo il grafico vuoto

    def get_luoghi(self):
        #legge luoghi dal dao
        if self._lista_luoghi is None: #se non gia letti
            self._lista_luoghi = DAO.read_all_luoghi()
        #costruisco anche dizionario nel Dubbio...
        for luogo in self._lista_luoghi:
            self.dizionario_luoghi[luogo.id] = luogo
        return self._lista_luoghi #restituisco lista, gia letta o letta adesso




    def crea_grafo(self):
        nodi = self.get_luoghi()
        #self.grafo.add_nodes_from(nodi)
        for n in nodi:
            self.grafo.add_node(n)

        #aggiungo i lati
        for i, u in enumerate(nodi):
            for v in nodi[i + 1:]:
                if len(DAO.check_if_u_and_v_connected(u.id, v.id)) > 0:
                    #aggiungi un arco tra u e v
                    print("ok")

