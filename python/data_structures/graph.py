class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self,value):
        new_vertex = Vertex(value)
        self.adjacency_list[new_vertex] = []
        return new_vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            raise KeyError
        edge = Edge(end_vertex, weight)
        list_of_edges = self.adjacency_list[start_vertex]
        list_of_edges.append(edge)

    def get_nodes(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def size(self):
        return len(self.adjacency_list)


class Vertex:
    def __init__(self,value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
