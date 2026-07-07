from interface.IAlgorithmn import IAlgorithmn
from collections import deque

class BFS(IAlgorithmn):
    graph = None

    def save(self, graph):
        self.graph = graph

    def run(self):
        self.path = []
        self.percorre_matriz(self.graph)

    
    def percorre_matriz(self, graph):
        if graph.data is None: return
        fila = deque()
        fila.append(graph)
        self.path.append(graph)

        while fila:
            atual = fila.popleft()
            for vizinho in atual.vizinhos:
                if self.notExistInList(vizinho):
                    fila.append(vizinho)
                    self.path.append(vizinho)
        


    def notExistInList(self, node):
        return node not in self.path



    def isConexo(self):
        print("\nVerificando Conexões . . .\n")
        self.run()
        nodes = []

        qtd_vertices = len(self.path)
        print(f"\tTotal de vertices: {qtd_vertices}\n")

        for node in self.path.copy():
            self.graph = node
            self.run()
            visited_vertice = len(self.path)
            data = {
                'address': node,
                'node': node.data,
                'visited': visited_vertice,
                'isConexo': True if visited_vertice == qtd_vertices else False
            }
            nodes.append(data)

        print("\tNodos\t\tQTD_visitados\t\tÉ Conexo")

        conexo = True
        for info in nodes:
            print(f"\tN({info['node']})\t\t({info['visited']}:{qtd_vertices})\t\t\t({'✓' if info['isConexo']else '✗'})")
            if not info['isConexo']:
                conexo  = False
        
        if conexo:
            print("\n\tⓘ Este grafo é conexo")
        else:
            print("\n\tⓘ Este grafo não é conexo")

        
    def TDE(self):
        print("_"* 150)
        print("\n")
        print("+"*50)
        print("BFS")
        print("+"*50)
        print("\n")
        print("_"* 150)
        self.printpath()
        print("_"* 150)
        self.isConexo()
        print("_"* 150)

    def printpath(self):
        print("Caminho gerado: ")
        lista = []
        for item in self.path:
            lista.append(str(item.data))
        
        print(" -> ".join(lista)) 
        print()   
