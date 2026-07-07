from algoritithms import (BFS, DFS, Biconnected, CPM, Kosaraju, Pert, Tarjan, TopologicalSort, TSP, Kruskal, Dijkstra, FloydWarshall)
from graph import (GKruskal, Graph, GDijkstra, GFloydWarshall)

class Contracts:

    
    algoritimos ={
        "BFS":  BFS,
        "DFS":  DFS,
        "Biconnected": Biconnected,
        "CPM": CPM,
        "Kosaraju": Kosaraju,
        "Pert": Pert,
        "Tarjan": Tarjan,
        "TopologicalSort": TopologicalSort,
        "TSP": TSP,
        'Kruskal': Kruskal,
        'Dijkstra': Dijkstra ,
        'FloydWarshall': FloydWarshall
    }


    graphs = {
        'Kruskal': GKruskal,
        'DFS': Graph,
        'BFS': Graph,
        'Dijkstra': GDijkstra,
        'FloydWarshall': GFloydWarshall
    }

    @classmethod
    def get_algorithm(cls, name:str):
        return cls.algoritimos[name]()

    @classmethod
    def get_graph(cls, name:str):
        return cls.graphs[name]()
