from interface.IAlgorithmn import IAlgorithmn

class FordFukerson(IAlgorithmn):
    source = None
    sink = None
    nodeList = []
    arestaList = []

    def save(self, data):
        self.source = data['source']
        self.sink = data['sink']
        self.nodeList = data['nodeList']
        self.arestaList = data['arestaList']

    def run(self):
        pass

    def TDE(self):
        self.printGraph()


    def printGraph(self):
        print(f"V({self.source.data}):", end='')
        for aresta in self.source.arestas:
            print(aresta.destino.data, end=' ')
        print()

        for node in self.nodeList:
            print(f"V({node.data}): ", end='')
            for aresta in node.arestas:
                print(aresta.destino.data,end=' ')
            print()
        
        print(f"V({self.sink.data})\n")

        print("\nArestasList")
        for aresta in self.arestaList:
            print(f"Destino: {aresta.destino.data}\tCapacidade: {aresta.capacidade}\tFluxo: {aresta.fluxo}")
