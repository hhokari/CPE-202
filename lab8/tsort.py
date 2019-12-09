#
# Emily Gavrilenko
# 015218875
# 6/5/2019
#
# Lab 8
# Section 12

from sys import argv
from stack_array import *

# Creates an object that stores the In Degree and Adjacent Vertices of a Vertice
class Vertice:
      def __init__(self):
          self.adjacent = []
          self.in_degree = 0


def tsort(vertices):
    verts = {}
    index = 0
    # Raises a value error if no input vertices
    length = len(vertices)
    if length == 0:
        raise ValueError("input contains no edges")
    # Raises a value error if there is an incomplete pair of vertices
    if length % 2 != 0:
        raise ValueError("input contains an odd number of tokens")
    # Goes through the list of vertices
    while index < length:
        # Stores the start and end vertex of each edge as key1 and key2
        key1 = vertices[index]
        key2 = vertices[index + 1]
        # Adds key1 and key2 to the dictionary of vertices if they're not already in it
        if key1 not in verts:
            verts[key1] = Vertice()
        if key2 not in verts:
            verts[key2] = Vertice()

        # Adds key2 as the adjacent vertex to key1
        vert1 = verts[key1]
        vert1.adjacent.append(key2)
        # Increases the In Degree of key2 since key1 goes into key2
        vert2 = verts[key2]
        vert2.in_degree += 1
        # Moves on to the next edge pair
        index += 2

    stack = Stack(len(verts))
    output = ""
    items = len(verts)

    # x = vertex data and y = vertex in_degree and adjacent vertices
    for x, y in verts.items():
        # if in_degree of a vertex is zero, the vertex key is added to the stack
        if y.in_degree == 0:
            stack.push(x)

    while items > 0:
        if stack.size() == 0:
            # Raises a ValueError if there is a cycle
            raise ValueError("input contains a cycle")

        # Pops the top item from the stack and decreases the in_degree value by one for each adjacent vertex of the popped vertex
        popped = stack.pop()
        vert_popped = verts[popped]
        adjacent_list = vert_popped.adjacent
        vert_popped.in_degree = None
        output += (popped + "\n")
        items -= 1
        for i in adjacent_list:
            if verts[i].in_degree is not None:
                verts[i].in_degree -= 1
            # x = vertex data and y = vertex in_degree and adjacent vertices
            for x in adjacent_list:
                # if in_degree of a vertex is zero, the vertex key is added to the stack
                if x not in stack.items:
                    if verts[x].in_degree == 0:
                        stack.push(x)
    return output

    #  Performs a topological sort of the specified directed acyclic graph.  The
    #  graph is given as a list of vertices where each pair of vertices represents
    #  an edge in the graph.  The resulting string return value will be formatted
    #  identically to the Unix utility {@code tsort}.  That is, one vertex per
    #  line in topologically sorted order.
    #
    #  Raises a ValueError if:
    #    - vertices is emtpy with the message "input contains no edges"
    #    - vertices has an odd number of vertices (incomplete pair) with the
    #      message "input contains an odd number of tokens"
    #    - the graph contains a cycle (isn't acyclic) with the message
    #      "input contains a cycle"


# def main():
#     '''Entry point for the tsort utility allowing the user to specify
#        a file containing the edge of the DAG'''
#     if len(argv) != 2:
#         print("Usage: python3 tsort.py <filename>")
#         exit()
#     try:
#         f = open(argv[1], 'r')
#     except FileNotFoundError as e:
#         print(argv[1], 'could not be found or opened')
#         exit()
#
#     vertices = []
#     for line in f:
#         vertices += line.split()
#
#     try:
#         result = tsort(vertices)
#         print(result)
#     except Exception as e:
#         print(e)
#
# if __name__ == '__main__':
#     main()
