lines = open("input.txt").read().split("\n")
alphabet = open("../libs/alphabet.txt").read()

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Node:
	def __init__(self, coords, letter, nodeId):
		self.coords = coords
		self.letter = letter
		self.score = 99999999
		self.nodeId = nodeId

	def GetCoords(self):
		return self.coords

	def GetLetter(self):
		return self.letter

	def SetLetter(self, letter):
		self.letter = letter

	def GetScore(self):
		return self.score

	def SetScore(self, score):
		self.score = score

	def GetId(self):
		return self.nodeId

nodes = []
unvisitedNodes = []
currentNode = 0
endNode = 0

def GetLowestNode(nodeList):
	global nodes
	lowestNode = nodeList[0]
	for node in nodeList:
		if (node.GetScore() < lowestNode.GetScore()):
			lowestNode = node
	return lowestNode.GetId()

def FindNeighbour(node, direction):
	global nodes
	if (direction == UP):
		if (node.GetCoords()[1] != 0):
			return nodes[node.GetId()-len(lines[0])].GetId()
	if (direction == RIGHT):
		if (node.GetCoords()[0] != len(lines[0])-1):
			return nodes[node.GetId()+1].GetId()
	if (direction == DOWN):
		if (node.GetCoords()[1] != len(lines)-1):
			return nodes[node.GetId()+len(lines[0])].GetId()
	if (direction == LEFT):
		if (node.GetCoords()[0] != 0):
			return nodes[node.GetId()-1].GetId()
	return -1

def RemoveFromUnvisited(nodeIndex):
	for i in range(len(unvisitedNodes)):
		if (unvisitedNodes[i].GetId() == nodeIndex):
			unvisitedNodes.pop(i)
			break

def GetLetterValue(letter):
	global alphabet
	return alphabet.find(letter)


nodeCounter = 0
for y in range(len(lines)):
	for x in range(len(lines[y])):
		node = Node([x, y], lines[y][x], nodeCounter)
		nodes.append(node)
		if (node.GetLetter() == "E"):
			endNode = node.GetId()
			node.SetLetter("z")
		if (node.GetLetter() == "S"):
			currentNode = node.GetId()
			node.SetScore(0)
			node.SetLetter("a")
		if (node.GetLetter() == "a"):
			currentNode = node.GetId()
			node.SetScore(0)
		unvisitedNodes.append(node)
		nodeCounter += 1

while len(unvisitedNodes) != 0:
	currentNode = GetLowestNode(unvisitedNodes)
	node = nodes[currentNode]
	neighbours = []
	neighbours.append(FindNeighbour(node, UP))
	neighbours.append(FindNeighbour(node, RIGHT))
	neighbours.append(FindNeighbour(node, DOWN))
	neighbours.append(FindNeighbour(node, LEFT))

	for neighbourIndex in neighbours:
		neighbour = nodes[neighbourIndex]
		if neighbour != -1:
			letterDelta = GetLetterValue(neighbour.GetLetter()) - GetLetterValue(node.GetLetter())
			if (letterDelta == 1 or letterDelta <= -1 or letterDelta == 0):
				if(neighbour.GetScore() > node.GetScore() + 1):
					neighbour.SetScore(node.GetScore() + 1)
	RemoveFromUnvisited(currentNode)

print(nodes[endNode].GetScore())