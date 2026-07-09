from interface.IAlgorithmn import IAlgorithmn

class pathFluxo:
    def __init__(self, caminho:list, ):
        self.caminho = caminho
        self.gargalo = self.definirGargalo()
    
    def definirGargalo(self):
        lista = []
        for node in self.caminho:
            lista.append(node.fluxo)
        return min(lista)


class FordFukerson(IAlgorithmn):
    source = None
    sink = None
    nodeList = []
    arestaList = []
    caminho = []
    pathGraphFluxo = None

    def save(self, data):
        self.source = data['source']
        self.sink = data['sink']
        self.nodeList = data['nodeList']
        self.arestaList = data['arestaList']

    def run(self):
        self.caminho = []
        self.pathGraphFluxo = None
        self.percorre(self.source, self.source.fluxo)

    def TDE(self):
        self.printGraph()
        self.printarCaminhos()


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
            print(f"Destino: {aresta.destino.data}\tCapacidade: {aresta.capacidade}\t")

    def percorre(self, nodo, fluxo):
        
        nodo.fluxo = fluxo

        self.caminho.append(nodo)
        if nodo == self.sink:
            self.salvarLista()
            return
            

        for aresta in nodo.arestas:
            if aresta.destino not in self.caminho:
                if aresta.capacidade < fluxo:
                    fluxo = aresta.capacidade

                self.percorre(aresta.destino, fluxo)
                self.caminho.remove(aresta.destino)
                fluxo = nodo.fluxo
        

            

        
        
    
    def salvarLista(self):
        newpath = pathFluxo(self.caminho.copy())
        if self.pathGraphFluxo is None or self.pathGraphFluxo.gargalo < newpath.gargalo:
            self.pathGraphFluxo = newpath
        

    
    def printarCaminhos(self):

        print()

        lista = []
        for nodo in self.pathGraphFluxo.caminho:
            lista.append(str((nodo.data, nodo.fluxo)))



        print(f"Caminho : ", end=' ')
        print(" -> ".join(lista))
        print(f"Gargalo: {self.pathGraphFluxo.gargalo}")
        print()