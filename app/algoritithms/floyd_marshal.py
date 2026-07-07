from interface.IAlgorithmn import IAlgorithmn


class FloydWarshall(IAlgorithmn):
    matriz = []
    vertices = []
    m_next = []
    qtd_vertices = 0
    caminho = []


    def save(self, graph):
        self.matriz = graph['matriz']
        self.vertices = graph['vertices']
        self.m_next = graph['next']
        self.qtd_vertices = len(self.vertices)


    def run(self):
        for intermediario in range(self.qtd_vertices):

            for origem in range(self.qtd_vertices):

                for destino in range(self.qtd_vertices):

                    if (self.matriz[origem][intermediario] != float('inf') 
                        and 
                        self.matriz[intermediario][destino] != float('inf')
                        ):
                        
                        distancia = self.matriz[origem][intermediario]  + self.matriz[intermediario][destino]

                        if distancia < self.matriz[origem][destino]:

                            self.matriz[origem][destino] = distancia
                            self.m_next[origem][destino] = self.m_next[origem][intermediario]
        

    def TDE(self):
        print("_"* 150)
        print("\n")
        print("+"*50)
        print("Floyd-Warshall")
        print("+"*50)
        print("\n")
        print("_"* 150)
        self.printMatrizPeso()
        print("_"* 150)
        self.printMatrizProximos()
        print("_"* 150)
        self.printCaminho()
        print("_"* 150)


    def printMatrizPeso(self):
        print("\nMatriz de Pesos: \n")

        print("\n\n",end='\t')
        for letra in self.vertices:
            print(letra, end='\t')
        print()


        for linha in range(self.qtd_vertices):
            print(self.vertices[linha], end='\t')
            for casa in self.matriz[linha]:
                print(f"{'∞' if casa == float('inf') else casa}", end='\t')
            print()
    
    def printMatrizProximos(self):
        print("\nMatriz de proximos valores: \n")

        print("\n\n",end='\t')
        for letra in self.vertices:
            print(letra, end='\t')
        print()


        for linha in range(self.qtd_vertices):
            print(self.vertices[linha], end='\t')
            for casa in self.m_next[linha]:
                print(f"{self.vertices[casa] if type(casa) is int else '-'}", end='\t')
            print()
        
    def printCaminho(self):
        print("\nDistancia de cada vértice:\n")
        print("\nORIGEM\tDESTINO\tDISTANCIA\tCAMINHO\n")
        for origem in range(self.qtd_vertices):
            for destino in range(self.qtd_vertices):
                caminho = self.reconstruirCaminho(origem, destino)
                distancia = '∞' if self.matriz[origem][destino] == float('inf') else self.matriz[origem][destino]
                start = self.vertices[origem]
                end = self.vertices[destino]
                if caminho is None:
                    print(f"   {start}\t   {end}\t   {distancia}\t\t sem caminho")
                else:
                    print(f"   {start}\t   {end}\t   {distancia}\t\t",'->'.join(caminho))


    

    def reconstruirCaminho(self, origem, destino):
        if self.m_next[origem][destino] is None:
            return None
        
        caminho = [self.vertices[origem]]
        while origem != destino:
            origem = self.m_next[origem][destino]
            caminho.append(self.vertices[origem])
        
        return caminho

