# class Graph:
#     def __init__(self):
#         self.vertices = []
#         self.edges = [[0,1,0,0,0,0,0],
#                       [0,0,1,1,0,0,0],
#                       [0,0,0,0,1,0,0],
#                       [0,0,0,0,0,1,1],
#                       [0,0,1,0,0,0,0],
#                       [0,0,1,0,0,0,0],
#                       [1,0,0,0,0,1,0]]
#     def add_vertex(self):
#         for v in range(len(self.edges)):
#             self.edges[v].append(0)
#         self.vertices.append([0] * (len(self.edges) + 1))
    
#     def print_matrix(self):
#         print(self.edges)

# g = Graph()

# g.print_matrix()

# print("------")

# g.add_vertex()

# g.print_matrix()


class Vertex:
    def __init__(self, value):
        self.value = value
        self.connections = {}
        
    def __str__(self):
        return f"{str(self.value)} connections: {str([v.value for v in self.connections])}"
    
    def add_connection(self, vert, weight=0):
        self.connections[vert] = weight
        
    def get_connections(self):
        return self.connections.keys()
  
    def get_value(self):
        return self.value

    def get_weight(self, vert):
        return self.connections[vert]
    

class Graph:
    def __init__(self):
        self.vertices = {}
        self.count = 0

    def __contains__(self, vert):
        return vert in self.vertices
    
    def __iter__(self):
        return iter(self.vertices.values())
    
    def add_vertex(self, value):
        new_vertex = Vertex(value)
        self.vertices[value] = new_vertex
        self.count += 1
        return new_vertex
    
    def remove_vertex(self, vert):
        if self.__contains__(vert):
            del self.vertices[vert]
            self.count -= 1
    
    def add_edge(self, v1, v2, weight=0):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_connection(self.vertices[v2], weight)

    def remove_edge(self):
        pass

    def get_vertices(self):
        return self.vertices.keys()
    
    
g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

g.add_edge("A", "B", 1)
g.add_edge("B", "C", 3)
g.add_edge("B", "D", 2)
g.add_edge("E", "D", 1)

for v in g:
  print(v)