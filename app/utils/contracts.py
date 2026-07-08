from algoritithms import (BFS, DFS,  Kruskal, Dijkstra, FloydWarshall, WelshPowell, FordFukerson)
from graph import (GKruskal, Graph, GDijkstra, GFloydWarshall, Gcolorido, GFordFukerson)

class Contracts:
    
    algoritimos ={
        1: BFS,
        2: DFS,
        3: Kruskal,
        4: Dijkstra ,
        5: FloydWarshall,
        6: WelshPowell,
        7: FordFukerson
    }


    graphs = {
        1: Graph,
        2: Graph,
        3: GKruskal,
        4: GDijkstra,
        5: GFloydWarshall,
        6: Gcolorido,
        7: GFordFukerson
    }

    @classmethod
    def get_algorithm(cls, name:int):
        return cls.algoritimos[name]()

    @classmethod
    def get_graph(cls, name:int):
        return cls.graphs[name]()
    
    @classmethod
    def getTotalAlgorithmn(cls):
        return len(cls.algoritimos) +1
