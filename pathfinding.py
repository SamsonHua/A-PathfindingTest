############################
#   Created by Samson H.   #
#  Sketchy A* Pathfinding  #
############################

# == Dependencies ==
import numpy as np
import math

#===================================
#             INPUTS
#===================================

#Input starting point here [x,y]
startingPoint = [1,1]
#Input target node here [x,y]
targetPoint = [6,4]

#===================================
#             CLASSES
#===================================
class Node:
    def __init__ (self,x,y):
        self.location = [x,y]
        self.x = x
        self.y = y
        self.coords = [x,y]
    parent = None
    g = 0
    h = 0
    f = 0
#===================================

#Store cells to be searched and cells that have already been searched
open_list = []
closed_list = []
blockages = [[2,2],[3,2],[4,2],[1,2]]

#===================================
#            FUNCTIONS
#===================================

#calculateH() calculates the H value for the A* algorithm 
def calculateH(node, targetPoint):
    x_dif = abs(node[0] - targetPoint[0])
    y_dif = abs(node[1] - targetPoint[1])
    distance = (math.sqrt((x_dif**2) + (y_dif**2))) * 10
    distance = math.trunc(distance)
    return distance


#calculateG() calculates the H value for the A* algorithm 
def calculateG(parentNode, node):
    x_dif = abs(parentNode.x - node[0])
    y_dif = abs(parentNode.y - node[1])
    distance = (math.sqrt((x_dif**2) + (y_dif**2))) * 10
    distance = math.trunc(distance)
    return distance


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
        newNode.g = int(parentNode.g) + int(calculateG(parentNode, node))
        newNode.h = int(calculateH(node, targetPoint))
        newNode.f = newNode.g + newNode.h
        newNode.parent = parentNode
        #Temporary Variable
        duplicateNode = "No"

        #Check for duplicate in open and closed list
        closedNodes = []

        for nodes in closed_list:
            closedNodes.append(nodes.coords)
        
        for index, nodes in enumerate(open_list):
            if newNode.coords == nodes.coords or newNode.coords in closedNodes:
                duplicateNode == "Yes"
                if newNode.f < nodes.f:
                    open_list[index] = newNode
            
        if duplicateNode == "No":
            nodeValues.append(newNode)

    return nodeValues

def nextNode():
    smallestF = [open_list[0].f]
    node_index = [0]

    for index, node in enumerate(open_list):
        #Skips index 0
        if index == 0:
            continue
        if node.f < smallestF[0]:
            #Clears index
            smallestF = []
            node_index = []
            #Re-assigns first index 
            node_index.append(index)
            smallestF.append(node.f)
        elif node.f == smallestF[0]:
            smallestF.append(node.f)
            node_index.append(index)
    
    #Check to see if there are matching f values
    if len(node_index) > 1:
        #Check for smallest h value
        smallestH = [open_list[node_index[0]].h]
        new_index = [0]

        for index, h_index in enumerate(node_index):
        #Skips index 0
            if h_index == 0:
                continue
            currentH = open_list[index].h
            if currentH < smallestH[0]:
                #Clears index
                smallestH = []
                new_index = []
                #Re-assigns first index 
                new_index.append(h_index)
                smallestH.append(open_list[index])
            elif currentH == smallestH[0]:
                smallestH.append(open_list[index])
                new_index.append(index)
        closed_list.append(open_list[new_index[0]])
        smallestNode = open_list[new_index[0]]
        open_list.pop(new_index[0])
        return smallestNode

    #Return smallest F value
    else:
        closed_list.append(open_list[node_index[0]])
        smallestNode = open_list[node_index[0]]
        open_list.pop(node_index[0])
        return smallestNode

def findPath(node):
    coordinates = [[node.x,node.y]]

    while node.parent != None:
        x = int(node.parent.x)
        y = int(node.parent.y)
        coords = [x,y]
        coordinates.append(coords)
        node = node.parent

    return coordinates
        
#Create pathfinding grid
rows = 7
columns = 7

#Create grid
grid = np.zeros((rows,columns))

#Start of algorithm (Add the starting point)
startingNode = Node(startingPoint[0],startingPoint[1])
closed_list.append(startingNode)

#Check for first set of nodes
locations = checkNodes(startingNode, grid)

calculatedNodes = calculateNodes(locations, startingNode)

for i in calculatedNodes:
    open_list.append(i)

#Print the f,h,g
# for nodes in open_list:
#     print(nodes.g)
#     print(nodes.h)
#     print(nodes.f)
#     print(nodes.coords)
#     print(nodes.parent)

#Determine the next square
current = nextNode()
# grid[current.x][current.y] = 8

#===================================
#              LOOP
#===================================

while True:
    if current.coords == targetPoint:
        break
    #Calculate locations
    locations = checkNodes(current, grid)
    calculatedNodes = calculateNodes(locations, current)

    for i in calculatedNodes:
        open_list.append(i)

    current = nextNode()
    # grid[current.x][current.y] = 8

steps = findPath(current)
steps.reverse()

for coordinates in steps:
    grid[coordinates[0]][coordinates[1]] = 9

print(steps)

#===================================
#             DISPLAY
#===================================

#Add starting point and end point to array, as well as blockages
grid[startingPoint[0]][startingPoint[1]] = 1
grid[targetPoint[0]][targetPoint[1]] = 2

for i in blockages:
    grid[i[0]][i[1]] = 7

#Show Grid
print(grid)