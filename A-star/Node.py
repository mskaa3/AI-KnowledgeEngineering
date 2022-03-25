
class Node:
    def __init__(self, num):
        self.num = num
        self.weight = 0
        self.successors = []
        self.h=0
        self.g=0
        self.predecessors=[]
        self.f=self.g+self.h

        self.parent=None


    def addSuccessors(self, successorsList: list):
        for i in successorsList:
            self.successors.append(i)

    def getNum(self):
        return self.num

    def getWeight(self):
        return self.weight

    def getH(self):
        return self.h

    def getSuccessors(self):
        return self.successors

    def getPredecessors(self):
        return self.predecessors

    def getSelf(self):
        return self



    def __str__(self):
        str1 = ""
        str2=" "
        for ele in self.successors:
            str1 += str(ele)+ " "
        for elem in self.predecessors:
            str2 += str(elem) + " "

        return 'Node:' + str(self.num) + ' weight ' + str(self.weight) + ' successors ' + str1 + 'h-value ' +str(self.h) + ' predecessors ' + str2
