from interface.IAlgorithmn import IAlgorithmn

class Kruskal(IAlgorithmn):
    graph = []

    def save(self, data):
        self.graph = data['graph']
        self.vertices = data['vertices']

    def run(self, graph):
        self.kruskal()

    def TDE(self):
        pass


    def kruskal(self):
        UnionFind(self.vertices)



class UnionFind:
    def __init__(self, nodes):
        self.parent = []

        for node in nodes:
            self.parent[node] = node
        
    
    def find(self,parent, node):
        while parent[node] != node:
            node = parent[node]
        
        return node

    def union(self, parent, node1, node2):

        root1 = self.find(parent, node1)
        root2 = self.find(parent, node2)

        if root1 != root2:
            parent[root2] = root1


        
