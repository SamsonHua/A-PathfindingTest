############################
#   Created by Samson H.   #
#  Sketchy A* Pathfinding  #
############################

# == Dependencies ==
import numpy as np

#===================================
#               INPUTS
#===================================

#Input starting point here [x,y]
startingPoint = [0,0]
#Input target node here [x,y]
targetPoint = [6,4]

#===================================
#               CLASSES
#===================================
class Node:
    def __init__ (self,x,y):
        self.location = [x,y]
        self.x = x
        self.y = y
    parent = None
    g = None
    h = None
    f = None
#===================================

#Store cells to be searched and cells that have already been searched
open_list = []
closed_list = []
blockages = [[2,2],[3,2],[4,2]]

#===================================
#               FUNCTIONS
#===================================

#calculateH() calculates the H value for the A* algorithm 
def calculateH():
    return None


#calculateG() calculates the H value for the A* algorithm 
def calculateG():
    return None


#checkNodes() only checks to see whether there is a blockage or the spot is non existent
def checkNodes(node, grid):
    #Check for column and row for matrix size
    columns = len(grid[0])
    rows = len(grid[1])

    #Terrible with for loops in python
    x = [-1,0,1]
    y = [-1,0,1]

    searchNodes = []
    
    for x_i in x:
        for y_i in y:
            #Skip the case with +0, -0 cause same square lol
            if x_i == 0 and y_i == 0:
                continue 
            coordinates = [node.x + x_i, node.y + y_i]
            #Check out of bounds search spots
            if ((node.x + x_i > columns - 1) or node.x + x_i < 0) or ((node.y + y_i > rows - 1 or node.y + y_i < 0)):
                continue
            #Check to see if any of the spots are blockages
            if coordinates in blockages:
                continue
            searchNodes.append(coordinates)
    #Returns list of cells to search
    return searchNodes

#calculateNodes() calculates the G score, H score, and F score based on the current nodes.
def calculateNodes(locations, parentNode):

    #Array to hold all the nodes
    nodeValues = []
    
    for node in locations:
        newNode = Node(node[0],node[1])
        newNode.g = parentNode.g + calculateG(parentNode, node)
        newNode.h = calculateH(parentNode, targetPoint)
        newNode.f = newNode.g + newNode.h
        #TODO Implement check for open & closed list
    
        nodeValues.append(newNode)

    return nodeValues

#Create pathfinding grid
rows = 7
columns = 7

#Create grid
grid = np.zeros((rows,columns))

#Start of algorithm (Add the starting point)
startingNode = Node(startingPoint[0],startingPoint[1])
closed_list.append(startingNode.location)

#Check for first set of nodes
locations = checkNodes(startingNode, grid)

open_list.append(calculateNodes(locations, startingNode))


print(locations)


#Add starting point and end point to array, as well as blockages
grid[startingPoint[0]][startingPoint[1]] = 1
grid[targetPoint[0]][targetPoint[1]] = 2

for i in blockages:
    grid[i[0]][i[1]] = 7

#Show Grid
print(grid)