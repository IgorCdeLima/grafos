# Grafos — Algoritmos de Teoria dos Grafos em Python

Aplicação de terminal que implementa e demonstra **sete algoritmos clássicos de Teoria dos Grafos**. A cada execução, o programa gera um grafo aleatório adequado ao algoritmo escolhido, executa o algoritmo e exibe passo a passo o grafo, as estruturas intermediárias (matrizes, tabelas de anteriores, listas de adjacência) e o resultado final.

> Projeto desenvolvido para a disciplina de **Teoria dos Grafos** da faculdade. Os métodos `TDE()` de cada algoritmo concentram a apresentação dos resultados pedidos nas atividades da disciplina.

---

## Sumário

- [Algoritmos implementados](#algoritmos-implementados)
- [Arquitetura](#arquitetura)
- [Tecnologias](#tecnologias)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como executar](#como-executar)
- [Apresentação dos algoritmos](#apresentação-dos-algoritmos)
- [Autor](#autor)

---

## Algoritmos implementados

| # | Algoritmo | Problema | Grafo gerado |
|:-:|---|---|---|
| 1 | **BFS** (busca em largura) | Percurso a partir de um vértice e verificação de conexidade | Dirigido, 10 vértices numéricos (1–19), arestas aleatórias |
| 2 | **DFS** (busca em profundidade) | Percurso recursivo e verificação de conexidade | Mesmo gerador do BFS |
| 3 | **Kruskal** | Árvore geradora mínima | Completo, não dirigido, 10 vértices, pesos de 1 a 36 |
| 4 | **Dijkstra** | Caminhos mínimos a partir de uma origem | Dirigido e ponderado, 10 vértices (letras), pesos de 1 a 36 |
| 5 | **Floyd-Warshall** | Caminhos mínimos entre todos os pares | Matriz de adjacência dirigida, 5 vértices, pesos de 1 a 20 |
| 6 | **Welsh-Powell** | Coloração de vértices | Não dirigido aleatório, 10 vértices, e o grafo fixo do *problema do zoológico* |
| 7 | **Ford-Fulkerson** | Caminhos de fluxo entre `SOURCE` e `SINK` | Rede com 10 vértices, fonte, sumidouro e capacidades de 1 a 20 |

### Detalhes de cada algoritmo

**BFS e DFS**
- Percorrem o grafo a partir do primeiro vértice gerado: o BFS com fila (`collections.deque`) e o DFS de forma recursiva.
- Exibem a ordem de visita dos vértices.
- Verificam a conexidade repetindo o percurso a partir de **cada um dos 10 vértices** do grafo. A tabela mostra quantos vértices cada um alcança. O grafo só é considerado conexo se todos os vértices alcançarem todos os outros (conexidade forte, já que o grafo é dirigido).

**Kruskal**
- Ordena todas as arestas pelo peso e as adiciona à árvore enquanto não formarem ciclo.
- A detecção de ciclo usa a estrutura **Union-Find** (`find`/`union`).
- Para ao atingir `V − 1` arestas e exibe a árvore geradora mínima.

**Dijkstra**
- Calcula a menor distância do primeiro vértice até todos os outros.
- Exibe a lista de adjacência e a tabela de anteriores, e responde a três itens:
  - **A)** distância mínima até cada vértice (`inf` para os inalcançáveis);
  - **B)** caminho mínimo até cada vértice, ou "sem caminho" quando ele não é alcançável;
  - **C)** caminho e distância até um destino sorteado entre os vértices alcançáveis.

**Floyd-Warshall**
- Programação dinâmica sobre a matriz de pesos, testando cada vértice como intermediário.
- Mantém uma **matriz de próximos** (`next`) para reconstruir os caminhos.
- Exibe as duas matrizes e a tabela completa de origem, destino, distância e caminho, indicando os pares sem caminho.

**Welsh-Powell**
- Ordena os vértices por grau decrescente e atribui a cada um a menor cor que nenhum vizinho usa.
- As cores são exibidas **coloridas no terminal** com a biblioteca `rich`, sorteadas em tons claros para ficarem legíveis em fundo escuro.
- Mostra a quantidade de cores usadas para dois grafos, ambos coloridos em ordem decrescente de grau: um aleatório e o grafo fixo do *problema do zoológico*, um exercício clássico de coloração em que animais incompatíveis não podem dividir o mesmo recinto.

**Ford-Fulkerson**
- Gera uma rede com vértices `SOURCE` (fluxo inicial 20) e `SINK`, e capacidades aleatórias nas arestas.
- Busca por DFS os caminhos simples da fonte ao sumidouro, calculando o **gargalo** (menor capacidade) de cada um.
- Exibe a rede, a lista de arestas com capacidades e o caminho escolhido, com o fluxo em cada vértice e o gargalo.

---

## Arquitetura

O projeto separa **algoritmos** de **geradores de grafo** por meio de duas interfaces, e um registro central liga cada opção do menu ao par correspondente:

```
                   ┌──────────────────────────┐
  main.py ───────► │  utils/contracts.py      │  opção do menu → (algoritmo, gerador)
  (menu)           │  Contracts               │
                   └────────────┬─────────────┘
               ┌────────────────┴────────────────┐
               ▼                                 ▼
   graph/  (IGraph)                    algoritithms/  (IAlgorithmn)
   createrGraph() → estrutura          save(grafo) → run() → TDE()
   do grafo aleatório                  recebe, executa e exibe
```

| Interface | Métodos | Papel |
|---|---|---|
| `IGraph` | `createrGraph()` | Gera o grafo aleatório no formato que o algoritmo espera (nós ligados, lista de arestas, lista de adjacência ou matriz) |
| `IAlgorithmn` | `save()`, `run()`, `TDE()` | Recebe o grafo, executa o algoritmo e apresenta os resultados |

Fluxo de uma execução (`main.py`):

```python
algorithm = Contracts.get_algorithm(opcao)
graph = Contracts.get_graph(opcao).createrGraph()
algorithm.save(graph)
algorithm.run()
algorithm.TDE()
```

Para adicionar um novo algoritmo, basta criar a classe do algoritmo (`IAlgorithmn`) e a do gerador (`IGraph`), e registrá-las com um novo número em `Contracts`.

---

## Tecnologias

| Ferramenta | Uso |
|---|---|
| Python 3.12 | Linguagem do projeto (imagem `python:3.12` no Docker) |
| [rich](https://github.com/Textualize/rich) | Saída colorida no terminal (coloração de Welsh-Powell) |
| `collections`, `random`, `copy`, `abc` | Biblioteca padrão: fila do BFS, geração aleatória, cópia de caminhos e interfaces |
| Docker / Docker Compose | Ambiente de execução reproduzível |

---

## Estrutura do projeto

```
grafos/
├── app/
│   ├── main.py                    # Menu interativo e laço principal
│   ├── interface/
│   │   ├── IAlgorithmn.py         # Interface dos algoritmos: save / run / TDE
│   │   └── IGraph.py              # Interface dos geradores: createrGraph
│   ├── utils/
│   │   └── contracts.py           # Registro: opção do menu → algoritmo + gerador
│   ├── graph/                     # Geradores de grafos aleatórios
│   │   ├── Graph.py               # Nós com lista de vizinhos (BFS / DFS)
│   │   ├── GraphKruskal.py        # Lista de arestas ponderadas
│   │   ├── GraphDijkstra.py       # Lista de adjacência ponderada
│   │   ├── GFloydMarshal.py       # Matriz de pesos e matriz de próximos
│   │   ├── Gcolorido.py           # Grafo aleatório e grafo do zoológico
│   │   └── GFordFukerson.py       # Rede com fonte, sumidouro e capacidades
│   └── algoritithms/              # Implementações dos algoritmos
│       ├── bfs.py
│       ├── dfs.py
│       ├── kruskal.py             # Inclui a estrutura Union-Find
│       ├── dijkstra.py
│       ├── floyd_marshal.py
│       ├── welsh_powell.py
│       └── FordFukerson.py
├── docker/
│   └── Dockerfile
├── docker-compose.yaml
└── requirements.txt
```

---

## Como executar

### Opção 1: com Docker (recomendado)

**Pré-requisitos:** Docker instalado e em execução.

- **Windows:** abra o **Docker Desktop** e aguarde até o status ficar **Running**.
- **Linux:** verifique se o serviço do Docker está ativo.

Na raiz do projeto, onde está o `docker-compose.yaml`, siga os passos abaixo.

**1. Construa a imagem.** Esse passo instala as dependências do `requirements.txt`:

```bash
docker compose build
```

**2. Abra um terminal dentro do container:**

```bash
docker compose run --rm graph-app bash
```

**3. Execute o programa:**

```bash
python app/main.py
```

O menu com os algoritmos é exibido. Digite o número do algoritmo (de **1** a **7**), veja o resultado e pressione **Enter** para voltar ao menu. Para sair, digite **0**. Qualquer outra entrada faz o programa pedir o número de novo.

Para sair do container, use `exit`. Como ele foi iniciado com `--rm`, é removido automaticamente.

**Observações:**
- Se o `requirements.txt` ou o `Dockerfile` forem alterados, rode `docker compose build` de novo.
- A pasta do projeto é montada como volume no container, então alterações no código-fonte não exigem reconstruir a imagem: basta rodar `python app/main.py` novamente.

### Opção 2: sem Docker

Com **Python 3.10 ou superior** instalado:

```bash
pip install rich
```

```bash
python app/main.py
```

---

## Apresentação dos algoritmos

Saídas reais de execuções do programa. Como os grafos são gerados aleatoriamente, vértices, arestas e pesos mudam a cada execução.

<!--
  Para adicionar a saída de um algoritmo:
  1. Rode "python app/main.py" e escolha o algoritmo.
  2. Copie a saída do terminal.
  3. Cole dentro do bloco ``` correspondente abaixo, no lugar do comentário.
  Se preferir uma imagem, troque o bloco por: <img src='imagens/nome.png'>
-->

### 1. BFS

```text
<!-- cole aqui a saída do BFS -->
```

### 2. DFS

```text
<!-- cole aqui a saída do DFS -->
```

### 3. Kruskal

```text
<!-- cole aqui a saída do Kruskal -->
```

### 4. Dijkstra

```text
<!-- cole aqui a saída do Dijkstra -->
```

### 5. Floyd-Warshall

```text
Matriz de Pesos:

        K       B       F       X       M
K       0       11      23      14      33
B       13      0       12      25      44
F       11      5       0       13      32
X       27      33      28      0       19
M       8       14      9       22      0

Distancia de cada vértice:

ORIGEM  DESTINO DISTANCIA       CAMINHO
   K       F       23            K->B->F
   K       M       33            K->X->M
   X       B       33            X->M->F->B
   M       X       22            M->K->X
```

### 6. Welsh-Powell

```text
<!-- cole aqui a saída do Welsh-Powell -->
```

### 7. Ford-Fulkerson

```text
<!-- cole aqui a saída do Ford-Fulkerson -->
```

---

## Autor

**Igor Cechinato de Lima**
GitHub: [@IgorCdeLima](https://github.com/IgorCdeLima)
