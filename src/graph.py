class Vertice:
    def __init__(self, nome):
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
            "Color: " + str(self.color) + "     " +
            "Fitness: " + str(self.fitness) + "     " +
            "Mapped Fitness: " + str(self.mappedFitness)
        )

class Grafo:
    def __init__(self, directed: bool = False):
        self.vertices = {}
        self.directed = directed

    def adiciona_vertice(self, nome_vertice) -> Vertice:
        # importante pois podem haver vertices que não tem arestas
        novo_vertice = Vertice(nome_vertice)
        self.vertices[nome_vertice] = novo_vertice
        return novo_vertice

    def adiciona_aresta(self, nome_origem, nome_destino):
        vertice_origem = self.obtem_vertice(nome_origem)
        vertice_destino = self.obtem_vertice(nome_destino)
        if not vertice_origem is None and not vertice_destino is None:
            vertice_origem.insere_adjacencias(vertice_destino)
            if not self.directed:
                vertice_destino.insere_adjacencias(vertice_origem)

    def obtem_vertice(self, nome_vertice) -> Vertice:
        if nome_vertice in self.vertices:
            return self.vertices[nome_vertice]
        else:
            return None

    def print_graph(self):
        for nome_vertice, vertice in self.vertices.items():
            print(f"vertice: \n    {vertice}")
            print("vizinhos: ")
            for nome_adj, adj in vertice.adjacencias.items():
                print(f"    {adj}")
            print("")
