from interface.IAlgorithmn import IAlgorithmn
from rich.console import Console

class WelshPowell(IAlgorithmn):
    graph = []
    cores = {}
    listaDeNodoComCor = {}
    zoologico = []
    console = Console()
    zooTDE = True


    def save(self, data):
        self.graph = data['graph']
        self.cores = data['cores']
        self.zoologico = data['zooGraph']

    def run(self):
        for node in self.graph:
            node.cor = self.escolhCor(node)


    def escolhCor(self,node):

        for num in range(len(self.cores)):
            disponivel = True
            for vizinho in node.vizinho:
                if num == vizinho.cor:
                    disponivel = False
                    break
                    
            if disponivel:
                return num

        novo_indice = len(self.cores)
        self.cores[novo_indice] = '#FFFFFF'

        return novo_indice


    def TDE(self):




        if self.zooTDE:

            print("_"* 150)        
            print("\n")
            print("+"*50)
            print("Grafos de Cores: Welsh Powell")
            print("+"*50)
            print("\n")
            print("_"* 150)
            print("\nGrafo Aleatório:\n")

        else:
            print("_"* 150)
            print("\nGrafo do problema do zoologico:\n")


        print("_"* 150)
        self.printGraph()
        print("_"* 150)
        self.minimoDeCores()
        print("_"* 150)

        
        if self.zooTDE:
            self.zooTDE = False

            self.graph = self.zoologico
            self.run()
            self.TDE()
        


    def printGraph(self):
        
        print("(NÓ)\t[GRAU]\t   [CORES]:\t VIZINHOS")
        for node in self.graph:
            self.console.print(f"\n({node.data})", style=self.cores[node.cor], end='')
            print(f"\t[{node.grau}]:", end='')
            self.console.print('\t█', style=self.cores[node.cor], end='')
            print(f"[{self.cores[node.cor]}]", end='')
            for vizinho in node.vizinho:
                self.console.print(f"\t{vizinho.data}", style=self.cores[vizinho.cor], end='')

        print()
    
    def printCores(self):
        print("\nCores Utilizadas:")
        for num in range(len(self.cores)-1):
            self.console.print(f"\n█: {self.cores[num]}",style=self.cores[num])
        print()

    def minimoDeCores(self):
        lista = set()
        for node in self.graph:
            lista.add(node.cor)
        
        self.minimo_cor = len(lista)
        print(f"Cores usadas: {self.minimo_cor} ")
        for cor in lista:
            self.console.print("█", style=self.cores[cor], end=' ')
            print(f"{self.cores[cor]}")


