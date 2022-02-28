# Code for an Adjacency List (Vertex + Graph)

# Creates Vertex for a Graph
class Vertex:
    
    # Sets id to be key & creates connectedTo to store adjacent vertices
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    # Adds neighboring vertex w/ weight of edge to connectedTo dictionary
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    # Outputs the connected vertices to the specified vertex
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # Returns all the vertices that the vertex is adjacent to
    def getConnections(self):
        return self.connectedTo.keys()

    # Returns the id of the vertex
    def getId(self):
        return self.id

    # Returns the weight of edge from current vertex to vertex passed
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

# Creates the Graph w/ the use of Vertex
class Graph:

    # Initializes vertList to store ADJACENT VERTICES
    # numVertices stores Total Vertices in the Graph
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    # Adds a Vertex to the Graph
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1 # Increments total vertices by one
        newVertex = Vertex(key) # Creates a new vertex w/ Vertex class
        self.vertList[key] = newVertex # Puts new vertex in vertList w/ corresponding key
        return newVertex

    # Finds a vertex & returns if its in Graph // None otherwise
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    # Allows for use of in syntaxing
    def __contains__(self,n):
        return n in self.vertList

    # Adds edge between two vertices (f - from; t - to)
    def addEdge(self,f,t,weight=0):
        # If f is not in the list of vertices, add it to vertList
        if f not in self.vertList:
            nv = self.addVertex(f)
        # If t is not in the list of vertices, add it to vertList
        if t not in self.vertList:
            nv = self.addVertex(t)
        # Make the neighbor of f be t along w/ the edge weight if specified
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    # Returns names of ALL VERTICES (keys) in the graph
    def getVertices(self):
        return self.vertList.keys()

    # Makes it easier to iterate over all vertex objects in a particular graph
    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
g.vertList
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
