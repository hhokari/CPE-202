#
#Emily Gavrilenko
#015218875
#6/10/2019
#
#Project 5
#Section 12

from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjacent_to = []
        self.visited = False
        self.color = None


# Reads the input file and creates a graph linking each two adjacent vertices with an edge
# The graph is not directed so each edge specified in the input file
# appears on the adjacency list of each vertex of the two vertices associated with the edge.
class Graph:
    def __init__(self, filename):
        self.vertices = {}
        file = open(filename, 'r')
        line = file.readline()
        while line is not "":
            vertices = line.split()
            key1 = vertices[0]
            key2 = vertices[1]
            if key1 not in self.vertices:
                vertex = Vertex(key1)
                self.vertices[vertex.id] = vertex
            if key2 not in self.vertices:
                vertex = Vertex(key2)
                self.vertices[vertex.id] = vertex
            vertex1 = self.vertices[key1]
            vertex2 = self.vertices[key2]
            vertex1.adjacent_to.append(vertex2.id)
            vertex2.adjacent_to.append(vertex1.id)
            line = file.readline()
        file.close()

    # Add vertex to graph, only if the vertex is not already in the graph.
    def add_vertex(self, key):
        if key in self.vertices:
            pass
        vertex = Vertex(key)
        self.vertices[key] = vertex
        # Add vertex to graph, only if the vertex is not already in the graph.

    # Return the Vertex object associated with the id. If id is not in the graph, return None
    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        return None

    # v1 and v2 are vertex id's.
    # add_edge connects v1 to v2 by updating their adjacency lists
    def add_edge(self, v1, v2):
        vertex1 = self.vertices[v1]
        vertex2 = self.vertices[v2]
        vertex1.adjacent_to.append(v2)
        vertex2.adjacent_to.append(v1)

    # Returns a list of id's representing the vertices in the graph, in ascending order
    def get_vertices(self):
        output = sorted(list(self.vertices))
        return output

    #    Returns a list of lists.  For example, if there are three connected components
    #    then you will return a list of three lists.  Each sub list will contain the
    #    vertices (in ascending order) in the connected component represented by that list.
    #    The overall list will also be in ascending order based on the first item of each sublist.
    #    This method uses Depth First Search logic!
    def conn_components(self):
        output = []
        # Steps through every vertex in the list
        for i in self.vertices:
            # If the vertex hasn't been visited, a depth search list is created for that vertex
            if self.vertices[i].visited is False:
                output.append(self.create_chain(self.vertices[i]))
        items = list(self.vertices.values())
        for i in items:
            i.visted = False
        edit = sorted(output)
        return edit


    # Returns a list of all visited vertices from the starting input vertex
    def create_chain(self, vertex):
        stack = Stack(len(self.vertices))
        chain = []
        # The first vertex is visited and added to the stack
        chain.append(vertex.id)
        stack.push(vertex)
        vertex.visited = True
        # Continues until every edge has been traveled
        while stack.size() > 0:
            # The first not visited vertex in the current vertex's adjacency list becomes next
            current = stack.peek()
            next = self.find_next(current.adjacent_to)
            # Visits the next vertex, adds it to the stack, and visits the next vertex
            # If there is no next vertex, remove the current vertex from the stack and seek another branch
            while next is not None:
                stack.push(next)
                chain.append(next.id)
                next.visited = True
                next = self.find_next(next.adjacent_to)
            stack.pop()
        # Sorts the chain and returns the resultant list
        output = sorted(chain)
        return output


    # Returns the first unvisited vertex in input adjacency list
    # Return None if all the vertices have been visited
    def find_next(self, adjacent):
        for i in adjacent:
            vertex = self.vertices[i]
            if vertex.visited is False:
                return vertex
        return None

    # Returns True if the graph is bicolorable and False otherwise.
    # This method uses Breadth First Search logic!
    def is_bipartite(self):
        # Steps through every vertex in the list
        for i in self.vertices:
            # If the vertex hasn't been visited, a breadth search list is created for that vertex
            # Returns True if the vertex's chain is bicolorable, and False otherwise
            if self.vertices[i].color is None:
                result = self.create_colors(self.vertices[i])
                if result is False:
                    break
        # Sets each vertex color back to None
        items = list(self.vertices.values())
        for i in items:
            i.color = None
        return result

    # Returns True if the passed vertex has a bicolorable chain, and False otherwise
    def create_colors(self, first_vertex):
        queue = Queue(len(self.vertices))
        # The beginning vertex in each chain is red
        first_vertex.color = "r"
        queue.enqueue(first_vertex)
        while queue.size() > 0:
            vertex = queue.dequeue()
            # The next color is the opposite of the current color, either red or black
            next_color = self.next_color(vertex)
            # Steps through every vertex in adjacency list
            # Each vertex must have an opposite color to the current vertex or False will return
            for i in vertex.adjacent_to:
                current = self.vertices[i]
                # If the vertex hasn't been assigned a color,
                # It is assigned an opposite color the current vertex and is enqueued to the queue
                if current.color is None:
                    current.color = next_color
                    queue.enqueue(current)
                # If the vertex already has a color and it's not opposite to the current color, return False
                elif current.color is not next_color:
                    return False
        return True

    # Determines the opposite color for the input vertex
    def next_color(self, vertex):
        if vertex.color == "r":
            return "b"
        if vertex.color == 'b':
            return 'r'
#
# def create_new_text(name):
#     file = open(name, 'w+')
#     file.write("v4 v5 \n")
#     file.write("v5 v6 \n")
#     file.write("v6 v4 \n")
#     file.write("v1 v2 \n")
#     file.write("v1 v3 \n")
#     file.close()

