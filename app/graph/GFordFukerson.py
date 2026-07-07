from interface.IGraph import IGraph
import random
import string

class Vertices:
    def __init__(self, data, tipo = None):
        self.data = data
        self.tipo = tipo
        self.arestas = []

class Aresta:
    def __init__(self, destino, capacidade = None):
        self.destino = destino
        self.capacidade = capacidade
        self.fluxo = 0


class GFordFukerson(IGraph):

    def createrGraph(self):
        QTD_VERTICES = 10

        datas = random.sample(string.ascii_uppercase, QTD_VERTICES)


        nodeList = [Vertices(datas[i]) for i in range(QTD_VERTICES)]
        arestaList = []

        sink = Vertices('SINK', 'SINK')
        exit = Vertices('EXIT', 'EXIT')


        for _ in range(0, QTD_VERTICES):
            vertice_aleatorio = random.randint(0,QTD_VERTICES-1)

            arestaList.append(
                    Aresta(
                        destino = nodeList[vertice_aleatorio],
                    )
            )
        
        for node in nodeList:
            for aresta in arestaList:
                if random.choice([True, False]) and aresta.destino != node and aresta.destino not in node.arestas:
                    aresta.capacidade = random.randint(0,20)
                    node.arestas.append(aresta)
        
        for aresta in nodeList:
            if random.choice([True, False, False, False, False]):
                aresta.capacidade = random.randint(0,20)
                sink.arestas.append(aresta)

        for _ in range(0, random.randint(1, 3)):
            arestaNum = random.randint(0,QTD_VERTICES-1)
            arestaList[arestaNum].capacidade =  random.randint(0,20)
            arestaList[arestaNum].destino = exit
        
    




        print(f"V({sink.data}):", end='')
        for aresta in sink.arestas:
            print(aresta.data, end=' ')
        print()

        for node in nodeList:
            print(f"V({node.data}): ", end='')
            for aresta in node.arestas:
                print(aresta.destino.data,end=' ')
            print()
        
        print(f"V({exit.data})\n")

        print("\nArestasList")
        for aresta in arestaList:
            print(f"Destino: {aresta.destino.data} Capacidade: {aresta.capacidade}")