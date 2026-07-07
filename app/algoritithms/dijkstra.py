from interface.IAlgorithmn import IAlgorithmn
from random import choice

class Aresta:
    def __init__(self, origem, destino, peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso


class Dijkstra(IAlgorithmn):

    lista_adj = {}
    node_list = []
    distancia = {}
    visitados = {}
    anterior = {}
    
    def save(self, graph):
        self.lista_adj = graph['adj']
        self.node_list = graph['vertices']
        

    def run(self):
        self.distancia = {}
        for node in self.node_list:
            self.distancia[node] = float('inf')

        origem = self.node_list[0]
        self.distancia[origem] = 0

        self.visitados = {}

        for node in self.node_list:
            self.visitados[node] = False

        self.anterior = {}
        
        for node in self.node_list:
            self.anterior[node] = None

        while True:


            menor_vertice = self.menorDistancia()

            if menor_vertice is None:
                break

            self.percorreVizinhos(menor_vertice)

            self.visitados[menor_vertice] = True

    









    def TDE(self):
        print("_"* 150)
        print("\n")
        print("+"*50)
        print("Dijkstra")
        print("+"*50)
        print("\n")
        print("_"* 150)

        self.printarInformacoes()
        print("_"* 150)
        self.imprimirTodosCaminhos()
        print("_"* 150)
        self.recosntruirTodosCaminhos()
        print("_"* 150)



    def printarInformacoes(self):

        print("\nLista de adjsascencia:\n")
        for iten in self.lista_adj:
            print(f"({iten}): {self.lista_adj[iten]}")

        print("_"* 150)

        print("\nTabela dos anteriores:\n")
        for iten in self.anterior:
            print(f"({iten}): {self.anterior[iten]}")
        
        print("_"* 150)

        print("\nA) Distancia minima:\n")
        for iten in self.distancia:
            print(f"({iten}): {self.distancia[iten]}")
        
        




    def menorDistancia(self):
        menor = float('inf')
        vertice_menor = None

        for vertice in self.distancia:
            if not self.visitados[vertice] and self.distancia[vertice] < menor:
                menor = self.distancia[vertice]
                vertice_menor = vertice
        
        return vertice_menor


    def percorreVizinhos(self, node):

        for vizinho, peso in self.lista_adj[node]:
            nova_distancia = self.distancia[node] + peso
            if nova_distancia< self.distancia[vizinho]:
                self.distancia[vizinho] = nova_distancia
                self.anterior[vizinho] = node


    def imprimirTodosCaminhos(self):
        print("\nB) Caminhos minimos:\n")
        
        for vertices in self.node_list:
            caminho = self.questionB(vertices)
            print(f"{vertices}: {'->'.join(caminho)}")

    def recosntruirTodosCaminhos(self):
        print("\nC)Caminho entre origem e destino:\n")

        destino = choice(self.node_list)

        self.questionC(destino)

    def questionB(self, destino):
        caminho = []

        atual = destino

        while atual is not None:
            caminho.append(atual)
            atual = self.anterior[atual]

        caminho.reverse()

        return caminho


    def questionC(self, destino):
        caminho = self.questionB(destino)

        print(f"Caminho até {destino}: {'->'.join(caminho)}")
        print(f"Distancia: {self.distancia[destino]}")


