
class Node:
    def __init__(self):
        self.weight = 0
        self.successors = []
        self.predecessors=[]
        self.h=0
        self.g=0
        self.f=self.g+self.h
        self.number = 0

        self.parent=None


    def addSuccessors(self, successorsList: list):
        for i in successorsList:
            self.successors.append(i)




    def __str__(self):
        str1 = ""
        for ele in self.successors:
            str1 += str(ele.number) + " "


        return 'Node:' + str(self.number) + ' weight ' + str(self.weight) + ' successors ' + str1 + 'h-value ' +str(self.h)
