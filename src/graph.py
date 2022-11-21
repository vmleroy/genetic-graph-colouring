class Vertice:
    def __init__(self, valor, nome: str = None):
        self.valor = valor
        self.nome = nome
        self.color = None
        self.fitness = None
        self.mappedFitness = None
        self.adjacencias = {}

    def insere_adjacencias(self, vizinho: "Vertice"):
        self.adjacencias[vizinho.nome] = vizinho

    def setFitness(self, fitnessFunction):
        self.fitness = fitnessFunction(self.x, self.y)

    def setMapFitness(self, linearMappingFunction, i, N):
        self.mappedFitness = linearMappingFunction(i, N)

    def __str__(self):
        return (
            "Nome: " + str(self.nome) + "     " +
            "Valor: " + str(self.valor) + "     " +
            "Color: " + str(self.color) + "     " +
            "Fitness: " + str(self.fitness) + "     " +
            "Mapped Fitness: " + str(self.mappedFitness)
        )

class Grafo:
    def __init__(self, directed: bool = False):
        self.vertices = {}
        self.directed = directed

    def adiciona_vertice(self, valor, nome_vertice: str = None) -> Vertice:
        # importante pois podem haver vertices que não tem arestas
        novo_vertice = Vertice(valor, nome_vertice)
        self.vertices[valor] = novo_vertice
        return novo_vertice

    def adiciona_aresta(self, valor_origem, valor_destino):
        vertice_origem = self.obtem_vertice(valor_origem)
        vertice_destino = self.obtem_vertice(valor_destino)
        if not vertice_origem is None and not vertice_destino is None:
            vertice_origem.insere_adjacencias(vertice_destino)
            if not self.directed:
                vertice_destino.insere_adjacencias(vertice_origem)

    def obtem_vertice(self, valor_vertice) -> Vertice:
        if valor_vertice in self.vertices:
            return self.vertices[valor_vertice]
        else:
            return None

    def print_graph(self):
        for valor_vertice, vertice in self.vertices.items():
            print(f"vertice: \n    {vertice}")
            print("vizinhos: ")
            for valor_adj, adj in vertice.adjacencias.items():
                print(f"    {adj}")
            print("")
