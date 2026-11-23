from dataclasses import dataclass

@dataclass
class Luogo:
    id: int
    nome: str
    tipo : str
    quota : int

    def __str__(self):
        return f"{self.id} {self.nome} {self.tipo} {self.quota} m"

    #nodi devono essere hashable per pèoter usare luoghi come nodi del grafo
    def __hash__(self):
        return hash(self.id)