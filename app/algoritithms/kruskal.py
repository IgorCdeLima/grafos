from interface.IAlgorithmn import IAlgorithmn

class Kruskal(IAlgorithmn):
    graph = []
    mst = []

    def save(self, data):
        self.graph = data['graph']
        self.vertices = data['vertices']

    def run(self, graph):
        self.kruskal()

    def TDE(self):
        for aresta in self.mst:
            print(f"Aresta: {aresta.origem} - {aresta.destino} | Peso: {aresta.peso}")


    def kruskal(self):
        uf = UnionFind(self.vertices)
        self.mst = []

        for aresta in self.graph:

            if uf.find(aresta.origem) != uf.find(aresta.destino):
                self.mst.append(aresta)
                uf.union(aresta.origem, aresta.destino)
            
            if len(self.mst) == len(self.vertices) - 1:
                break
            
        
                




class UnionFind:
    def __init__(self, nodes):
        self.parent = {}

        for node in nodes:
            self.parent[node] = node
        
        print(self.parent)
        
    
    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        
        return node

    def union(self, node1, node2):

        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            self.parent[root2] = root1


        
