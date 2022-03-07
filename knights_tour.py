# Code for Solving the Knight's Tour using Graphs

from adjacency_list import Graph

# Establishes the knightGraph given a board size (n-by-n)
def knightGraph(bdSize):
    ktGraph = Graph()
    # Makes a pass over the entire board
    for row in range(bdSize):
       for col in range(bdSize):
           # Gets nodeId & newPositions by calling helper functions
           nodeId = posToNodeId(row,col,bdSize)
           newPositions = genLegalMoves(row,col,bdSize)
           # Goes through legal moves & adds an edge from the current position to the legal moves
           for e in newPositions:
               nid = posToNodeId(e[0],e[1],bdSize)
               ktGraph.addEdge(nodeId,nid)
    return ktGraph

# Converts location on board in terms of a row & column into a linear vertex number
def posToNodeId(row, column, board_size):
    return (row * board_size) + column

# Generates the legal moves from a given position on the board
def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    # Goes through each offset and adds it to current position to generate new positions
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        # If the newX & newY coordinates are legal coordinates, it is appended to newMoves
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

# Makes sure a particular move that is generated is still on the board
def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize: # Checks to see if x is within 0 & board size
        return True
    else:
        return False

# Function that completes the Knight's Tour
def knightTour(n,path,u,limit):
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections())
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:  # prepare to backtrack
                path.pop()
                u.setColor('white')
        else:
            done = True
        return done

# Speeds up knightTour by choosing vertices that has the fewest available moves
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0]) # CRITICAL LINE
    return [y[1] for y in resList]
