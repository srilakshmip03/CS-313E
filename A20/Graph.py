import sys

class Stack(object):
    def __init__(self):
        self.stack = []
    
    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)
    
    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()
    
    # check the item on the top of the stock
    def peek(self):
        return self.stack[-1]
    
    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)
    
    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

class Queue(object):
    def __init__(self):
        self.queue = []
    
    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
    
    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)
    
    # check the item on the top of the stock
    def peek(self):
        return self.queue[0]
    
    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)
    
    # return the number of elements in the queue
    def size(self):
        return len(self.queue)

# class for Vertex object
class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False
    
    # determine if a vertex was visited
    def was_visited(self):
        return self.visited
    
    # determine the label of the vertex
    def get_label(self):
        return self.label
    
    # string representation of the vertex
    def __str__(self):
        return str(self.label)

class Graph (object):
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []
    
    def __str__(self):
        string = ''
        nVert = len(self.Vertices)
        for i in range(nVert):
            for j in range(len(self.adjMat[i])):
                string += str(self.adjMat[i][j]) + ' '
            string += '\n'
        return string

    # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex (self, label):
        if (self.has_vertex (label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)

    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # do a depth first search in a graph
    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push (u)

        # the stack is empty, let us reset the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs (self, v):
        # create the Queue
        theQueue = Queue()

        # mark the vertex v as visited and enqueue
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theQueue.enqueue(v)

        # visit all the other vertices according to depth
        while (not theQueue.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theQueue.peek())
            if (u == -1):
                u = theQueue.dequeue()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theQueue.enqueue(u)

        # the queue is empty, let us reset the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False
    
    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        f_index = self.get_index(fromVertexLabel)
        t_index = self.get_index(toVertexLabel)
        self.adjMat[f_index][t_index] = 0
        self.adjMat[t_index][f_index] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        if (self.has_vertex(vertexLabel)):
            i = self.get_index(vertexLabel)
            # remove vertex from vertices list
            self.Vertices.pop(i)
            # remove vertex row in adjMat
            self.adjMat.pop(i)
            # remove vertex column in remaining vertices
            for j in range(len(self.Vertices)):
                (self.adjMat[j]).pop(i)

def main():
    # create the Graph object
    cities = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int (line)

    # read the vertices to the list of Vertices
    for i in range (num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        cities.add_vertex (city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int (line)

    # read each edge and place it in the adjacency matrix
    for i in range (num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start = int (edge[0])
        finish = int (edge[1])
        weight = int (edge[2])

        cities.add_directed_edge (start, finish, weight)

    # read the starting vertex for dfs and bfs
    line = sys.stdin.readline()
    start_vertex = line.strip()

    # get the index of the starting vertex
    start_index = cities.get_index (start_vertex)

    # get the two vertex labels for delete edge test
    line = sys.stdin.readline().split(' ')
    from_vertex = line[0]
    to_vertex = line[1]

    # get the vertex label for deleting a vertex
    line = sys.stdin.readline()
    d_vertex = line.strip()

    # do the depth first search
    print ("Depth First Search")
    cities.dfs(start_index)
    print ()

    # test breadth first search
    print ("Breadth First Search")
    cities.bfs(start_index)
    print ()

    # test deletion of an edge
    print("Deletion of an edge")
    cities.delete_edge(from_vertex, to_vertex)
    print()
    print("Adjacency Matrix")
    print(cities)
    print()

    # test deletion of a vertex
    print("Deletion of a vertex")
    cities.delete_vertex(d_vertex)
    print()
    print("List of Vertices")
    for v in range(len(cities.Vertices)):
        print(cities.Vertices[v])
    print()
    print("Adjacency Matrix")
    print(cities)
    
if __name__ == "__main__":
    main()