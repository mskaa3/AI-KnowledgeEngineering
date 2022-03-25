from Node import Node


class Graph:
    def __init__(self):
        self.nodesNum = 0
        self.nodeList = []

    def addNode(self, node: Node):
        self.nodeList.append(node)
        self.nodesNum += 1

    def getGraphSize(self):
        return self.nodesNum

    def getNode(self, index):
        return self.nodeList[index]

    def getNodeByName(self, name):
        for elem in self.nodeList:
            if elem.getNum() is name:
                 index=self.nodeList.index(elem)

        return self.nodeList[index]