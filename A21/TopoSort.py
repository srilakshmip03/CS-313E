#  File: TopoSort.py

#  Description: Topological sort and detect cycles

#  Student Name: Srilakshmi Palanikumar

#  Student UT EID: sp49694  

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 11-28-22

#  Date Last Modified: 

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

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False
    self.in_degree = 0

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if not self.has_vertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
      
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  def mod_adj_unvisited_vertex (self, stack):
    nVert = len(self.Vertices)
    v = stack.peek()
    for i in range (nVert):
      if (self.adjMat[v][i] > 0 and (self.Vertices[i]).was_visited()):
        if (stack.is_inside(i)):
          return -2
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  def delete_vertex (self, vertexLabel):
    vertex=self.get_index(vertexLabel)
    for i in range(len(self.adjMat)):
      del(self.adjMat[i][vertex])
    del(self.adjMat[vertex])
    del(self.Vertices[vertex])

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

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do breadth first search in a graph
  def bfs (self, v):
      # create a queue
      qu = Queue()

      # mark the starting vertex as visited and enqueue it
      self.Vertices[v].visisted = True
      qu.enqueue(v)

      # visit all other vertices according to breadth
      while (not qu.is_empty()):
          # get an adjacent unvisited vertex
          u = self.get_adj_unvisited_vertex(qu.peek())
          if (u == 1):
              u = qu.dequeue
          else:
              # visit the next vertex
              self.Vertices[u].visited = True
              qu.enqueue(u)

      # the queue is empty, let us rest the flags
      nVert = len (self.Vertices)
      for i in range (nVert):
          (self.Vertices[i]).visited = False

  # determine if a directed graph has a cycle
  def has_cycle (self):
        # create a List
        theList = []
        # create starting vertex v
        v = 0

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        theList.append(v)

        # visit all the other vertices according to depth
        while (len(theList) != 0):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theList[-1])
            if (u == -1):
                u = theList.pop(-1)
            else:
                (self.Vertices[u]).visited = True
                theList.append(u)
                # check to see if any previously visited vertices have an edge
                # to vertex u
                for i in range(len(theList)):
                    if (self.adjMat[u][i] != 0):
                        return True

        # the list is empty, let us reset the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False
        
        return False

  # return a list of vertices after a topological sort
  def toposort (self):
    visited = []

    while (self.Vertices):
      deleted = []
      v = 0

      while(v < len(self.Vertices)):
        is_visited = False

        vertex = self.Vertices[v].label
        for i in range(len(self.Vertices)):
          if(self.adjMat[i][v] != 0):
            is_visited = True
            break

        if(is_visited):
          v += 1

        else:
          visited.append(vertex)
          deleted.append(vertex)
          v += 1

        while(deleted):
          self.delete_vertex(deleted[0])
          deleted.pop(0)

    # the list is empty, let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
        (self.Vertices[i]).visited = False
    
    return visited   

def main():
  # create a Graph object
  theGraph = Graph()

  # add vertices
  nVert = int (sys.stdin.readline().strip())
  for i in range (nVert):
    letter = (sys.stdin.readline()).strip()
    theGraph.add_vertex (letter)

  # read the edges
  nEdges = int ((sys.stdin.readline()).strip())
  for i in range (nEdges):
    line = sys.stdin.readline().strip()
    edge = line.split(" ")
    fIndex = theGraph.get_index(edge[0])
    tIndex = theGraph.get_index(edge[1])
    theGraph.add_directed_edge (fIndex, tIndex)

  if theGraph.has_cycle == True:
    str = "has"

  else:
    str = "does not have"
  
  print ("The Graph " + str + " a cycle.")
  
  if str == "has":
    return

  print ("List of vertices after toposort")
  print(theGraph.toposort())
    
if __name__ == "__main__":
  main()