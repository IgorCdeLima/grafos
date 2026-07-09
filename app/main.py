from utils.contracts import Contracts
import sys
import os

def runApp(name):
    name_algorithmn = name

    algorithm = Contracts.get_algorithm(name_algorithmn)
    graph = Contracts.get_graph(name_algorithmn).createrGraph()
    algorithm.save(graph)
    algorithm.run()
    algorithm.TDE()

def info():
    print("=" * 100)
    print("Algoritmos de percurso de grafo:")
    print("_" * 100)
    print("[1] BFS\n[2] DFS\n[3] Kruskal\n[4] Dijkstra\n[5] Floyd Warshall\n[6] Welsh Powell\n[7] Ford Fukerson\n[0] Sair")
    print("_" * 100)
    runApp(chooseNumber())
    input("\nPress Enter to  continue...")


def chooseNumber():
    algorithmn = input("Qual você quer testar: ")
    print("=" * 100)
    if not algorithmn.isdecimal() or  (0 > int(algorithmn) > Contracts.getTotalAlgorithmn()):
        algorithmn = chooseNumber()
        
    if int(algorithmn) == 0:
        sys.exit(0)

    
    return int(algorithmn)

def limparTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")

if __name__ == '__main__':

    while True:

       limparTerminal()
       info()

