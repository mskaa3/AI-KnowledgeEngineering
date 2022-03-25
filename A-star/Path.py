from Node import Node


class Path:
    def __init__(self):
        self.totalWeight = 0
        self.nodes = []

    def addNode(self, node: Node):
        self.nodes.append(node)
        self.totalWeight += node.weight

    def getNode(self, index):
        return self.nodes[index]

    def deleteLast(self):
        self.totalWeight -= self.nodes[-1].weight
        del self.nodes[-1]
        return self