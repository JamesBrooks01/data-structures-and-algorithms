from data_structures.queue import Queue
from data_structures.stack import Stack

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
        return list(self.adjacency_list.keys())

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def size(self):
        return len(self.adjacency_list)

    def breadth_first(self, vertex):
        if self.adjacency_list == {}:
            return []
        vertice_queue = Queue()
        traversed_vertices = []
        final_list = []
        vertice_queue.enqueue(vertex)
        traversed_vertices.append(vertex)
        final_list.append(vertex.value)
        while vertice_queue.is_empty() == False:
            current_vertex = vertice_queue.dequeue()
            neighbors = self.get_neighbors(current_vertex)
            for edge in neighbors:
                if edge.vertex not in traversed_vertices:
                    vertice_queue.enqueue(edge.vertex)
                    traversed_vertices.append(edge.vertex)
                    final_list.append(edge.vertex.value)
        return final_list

    def depth_first_search(self, vertex):
        if self.adjacency_list == {}:
            return []
        def traverse(node):
            final_list.append(node.value)
            neighbors = self.get_neighbors(node)
            for edge in neighbors:
                if edge.vertex.visited == 0:
                    edge.vertex.visited = 1
                    node.visited = 1
                    traverse(edge.vertex)

        final_list = []
        traverse(vertex)
        return final_list

class Vertex:
    def __init__(self,value, visited=0):
        self.value = value
        self.visited = visited

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
