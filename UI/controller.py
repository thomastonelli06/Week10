import flet as ft

class Controller:
    def __init__(self, view, model):
        self.model = None
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        # ottnere luoghi del grafo e li chiedo al model

        self.model.crea_grafo()
        print(self.model.crea_grafo)


    def handle_visita_ampiezza(self, e):
        pass

    def handle_visita_profondita(self, e):
        pass
