from algoritithms import (BFS, DFS,  Kruskal, Dijkstra, FloydWarshall, WelshPowell, FordFukerson)
from graph import (GKruskal, Graph, GDijkstra, GFloydWarshall, Gcolorido, GFordFukerson)

class Contracts:

    
    algoritimos ={
        "BFS":  BFS,
        "DFS":  DFS,
        'Kruskal': Kruskal,
        'Dijkstra': Dijkstra ,
        'FloydWarshall': FloydWarshall,
        'WelshPowell':WelshPowell,
        'FordFukerson': FordFukerson
    }


    graphs = {
        'Kruskal': GKruskal,
        'DFS': Graph,
        'BFS': Graph,
        'Dijkstra': GDijkstra,
        'FloydWarshall': GFloydWarshall,
        'WelshPowell': Gcolorido,
        'FordFukerson': GFordFukerson
    }

    @classmethod
    def get_algorithm(cls, name:str):
        return cls.algoritimos[name]()

    @classmethod
    def get_graph(cls, name:str):
        return cls.graphs[name]()
