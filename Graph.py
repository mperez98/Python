#  File: Graph.py

#  Description: This program creates a graph from input data and displays an adjacency matrix and test deleting a vertex and edge.

#  Student Name: Mathew Perez

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 04/23/2018

#  Date Last Modified: 04/23/2018

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
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
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    theStack.push (v)

    return_list = []
    return_list.append(self.Vertices[v].getLabel())
    
    
    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])

        return_list.append(self.Vertices[u].getLabel())

        theStack.push(u)
    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    return return_list

  # do breadth first search in a graph
  def bfs (self, v):
    # create a Queue
    theQueue = Queue ()

    # mark vertex v as visited
    (self.Vertices[v]).visited = True
    print(self.Vertices[v])
    theQueue.enqueue(v)

    return_list = []
    return_list.append(self.Vertices[v].getLabel())

    # visit other vertices according to breadth
    while (not theQueue.isEmpty()):
      # get all adjacent unvisited vertices of the current vertex
      u = self.getAdjUnvisitedVertex (theQueue.queue[0])
      
      if (u == -1):
        u = theQueue.dequeue()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        return_list.append(self.Vertices[u].getLabel())

        theQueue.enqueue(u)
        
        
    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    return return_list

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    weight = self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)]
    if (weight == 0):
      return -1
    else:
      return weight

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    neighbor_lst = []
    for i in range (len(self.Vertices)):
      if (self.adjMat[self.getIndex(vertexLabel)][i] > 0):
        neighbor_lst.append(i)
    return neighbor_lst

  # get a copy of the list of vertices
  def getVertices (self):
    copy = []
    for i in range (len(self.Vertices)):
      copy.append(self.Vertices[i].getLabel())
    return copy

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    self.adjMat[self.getIndex(fromVertexLabel)][self.getIndex(toVertexLabel)] = 0
    self.adjMat[self.getIndex(toVertexLabel)][self.getIndex(fromVertexLabel)] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    # find index of vertex to be deleted
    idx = self.getIndex(vertexLabel)

    # delete corresponding column in adjacency matrix
    for i in range (len(self.adjMat)):
      del self.adjMat[i][idx]

    # delete corresponding row in adjacency matrix
    del self.adjMat[idx]

    # delete vertex from vertices list
    del self.Vertices[self.getIndex(vertexLabel)]

def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  inFile = open ("./graph.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())
  print (numVertices)

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    print (city)
    cities.addVertex (city)

  # read the edges
  numEdges = int ((inFile.readline()).strip())
  print (numEdges)

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.addDirectedEdge (start, finish, weight)

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()

  # read the starting vertex for dfs and bfs
  startVertex = (inFile.readline()).strip()
  print (startVertex)

  # get the index of the start Vertex
  startIndex = cities.getIndex (startVertex)
  print (startIndex)

  # do depth first search
  print ("\nDepth First Search from " + startVertex)
  print(cities.dfs (startIndex))
  print()

  # test breadth first search
  print ("\nBreadth First Search from " + startVertex)
  print(cities.bfs(startIndex))
  print()

  # test deletion of an edge
  del_edge = (inFile.readline()).split()
  del_edge_from = del_edge[0]
  del_edge_to = del_edge[1]
  print("\nTest Deletion of Edge from " + del_edge_from + " to " + del_edge_to)
  cities.deleteEdge(del_edge_from, del_edge_to)
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()

  # test deletion of a vertex
  del_vert = (inFile.readline()).strip()
  print(del_vert)
  print("\nTest Deletion of a Vertex -", del_vert)
  cities.deleteVertex(del_vert)
  for i in range (len(cities.Vertices)):
    for j in range (len(cities.Vertices)):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()


  inFile.close()

if __name__ == "__main__":
  main()


