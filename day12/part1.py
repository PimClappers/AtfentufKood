lines = open("input2.txt").read().split("\n")

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
	lowestNode = nodeList[0]
	for node in nodeList:
		if (node.GetScore() < lowestNode.GetScore()):
			lowestNode = node
	return lowestNode.GetId()


nodeCounter = 0
for y in range(len(lines)):
	for x in range(len(lines[y])):
		node = Node([x, y], lines[y][x], nodeCounter)
		nodes.append(node)
		if (node.GetLetter() == "E"):
			endNode = node.GetId()
		if (node.GetLetter() == "S"):
			currentNode = node.GetId()
			node.SetScore(0)
		else:
			unvisitedNodes.append(node)
		nodeCounter += 1

print(len(nodes))
print(len(unvisitedNodes))

print (GetLowestNode(unvisitedNodes))
# while len(unvisitedNodes) != 0:
# 	nodeIndex = GetLowestNode(unvisitedNodes)