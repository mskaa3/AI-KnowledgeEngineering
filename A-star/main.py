from Graph import Graph
from Node import Node
from Path import Path
import time


def createGraph(fileName, str):
    with open(fileName) as f:
        lines = f.readlines()
    count = 0
    ind = 0
    for line in lines:
        count += 1

        if count == 1:
            graphNodes = int(line)

            graphName = Graph()
            for i in range(graphNodes):
                graphName.addNode(Node(i))
            finalNode = Node(-1)
            finalNode.weight = 0.0
            startNode = Node(-2)
            startNode.weight = 0.0
            graphName.addNode(startNode)
            graphName.addNode(finalNode)

        if count > 1 and count < graphNodes + 2:
            graphName.nodeList[count - 2].weight = float(line)

        if count >= graphNodes + 2:
            numList = list(line.split(" "))
            ints = []
            for element in numList:
                ints.append(int(element))
            graphName.nodeList[ind].addSuccessors(ints)
            ind += 1
    startList = findStarts(graphName)
    startList.remove(-2)
    startNode.addSuccessors(startList)
    for i in startList:
        if i is not -2:
            for elem in graphName.nodeList:
                if elem.getNum() is i:
                    elem.predecessors.append(-2)
    if str is 'children':
        start=time.time_ns()
        childHeuristics(graphName)
        finish=time.time_ns()
        timeFIN=finish-start
        print(f' time of heuristics calculation for ChildrenAvg is in nanoSec:')
        print("%.20f" % timeFIN )
    if str is 'dfs':
        start = time.time_ns()
        DFSheuristics(graphName)
        finish = time.time_ns()
        timeFIN = finish - start
        print(f' time of heuristics calculation for DFS is in nanoSec:')
        print("%.20f" % timeFIN)

    if str is "dfs+":
        start = time.time_ns()
        DFSPLUSheuristics(graphName)
        finish = time.time_ns()
        timeFIN = finish - start
        print(f' time of heuristics calculation for DFS+ is in nanoSec:')
        print("%.20f" % timeFIN)
    if str is "childrenparent":
        start = time.time_ns()
        childParentHeuristics(graphName)
        finish = time.time_ns()
        timeFIN = finish - start
        print(f' time of heuristics calculation for Children&parents  is in nanoSec:')
        print("%.20f" % timeFIN)


    return graphName



def find(node: Node,graph:Graph,finalNode:Node):
    start = time.time_ns()
    open = []
    closed=[]
    node.g=node.weight
    open.append(node)

    while len(open) is not 0:
        curNode = open[0]
        ind = 0
        for elem in open:
            # we are searching for the element with the biggest f value on the open list
            if elem.f > curNode.f:
                curNode = elem
                ind = open.index(elem)
        # and we pop it
        open.pop(ind)
        # if its the final node, that traversback to recreate the path
        if curNode is finalNode:
            path = Path()
            while curNode.parent != None:
                path.addNode(curNode)
                curNode = curNode.parent
            finish = time.time_ns()
            timeFIN = finish - start
            print(f' time of searching')
            print("%.20f" % timeFIN)
            return path


        else:
            suc = curNode.getSuccessors()
            suc2 = []
            for elem in suc:
                suc2.append(graph.getNode(int(elem)))
            for child in suc2:


                candidateWeight=curNode.g+curNode.weight
                if  candidateWeight>=child.g:
                    # assign parent to a child
                    child.parent = curNode
                    closed.append(child)
                    # traversed path as a parents traversed path
                    child.g= candidateWeight
                    child.f=child.g+child.h
                    # adding children to the open to iterate through them and finding the highest f value
                    if child not in open:
                        open.append(child)



def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        suc = node.getSuccessors()
        suc2 = []
        for elem in suc:
            suc2.append(graph.getNode(int(elem)))
        for neighbour in suc2:
            dfs(visited, graph, neighbour)


def DFSheuristics(graph: Graph):
    for elem in graph.nodeList:
        visited=set()
        dfs(visited,graph,elem)
        elem.h=len(visited)

def DFSPLUSheuristics(graph: Graph):
    for elem in graph.nodeList:
        visited=set()
        dfs(visited,graph,elem)
        elem.h=len(visited)+elem.weight

def childParentHeuristics(graph: Graph):
    for elem in graph.nodeList:
        elem.h=len(elem.getPredecessors())+len(elem.getSuccessors())



def childHeuristics(graph: Graph):
    for elem in graph.nodeList:
        hValue = 0
        children = elem.getSuccessors()
        if len(children) is not 0:
            for i in children:
                hValue += graph.getNode(int(i)).weight
            # hValue = hValue / len(children)

        hValue+=elem.weight
        elem.h = hValue


def findStarts(graph: Graph):
    for elem in graph.nodeList:
        for inListElement in graph.nodeList:
            num = elem.getNum()
            successors = inListElement.getSuccessors()
            if num in successors:
                elem.predecessors.append(inListElement.getNum())
    startList = []
    for element in graph.nodeList:
        if len(element.getPredecessors()) is 0:
            startList.append(element.getNum())
    return startList


if __name__ == '__main__':
    print('----------------------------File test.txt-------------------------')
    print('')
    firstGraphDFS = createGraph('test.txt', 'dfs')
    pathDFS = find(firstGraphDFS.getNodeByName(-2), firstGraphDFS, firstGraphDFS.getNodeByName(-1))
    print(f'Total weight in DFS {pathDFS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createGraph('test.txt', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS.getNodeByName(-2), firstGraphDFSPLUS, firstGraphDFSPLUS.getNodeByName(-1))
    print(f'Total weight in DFS+ {pathDFSPLUS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createGraph('test.txt', 'children')
    pathCHILDREN = find(firstGraphCHILDREN.getNodeByName(-2), firstGraphCHILDREN, firstGraphCHILDREN.getNodeByName(-1))
    print(f'Total weight in CHILDREN {pathCHILDREN.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createGraph('test.txt', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT.getNodeByName(-2), firstGraphCHILDRENPARENT,
                              firstGraphCHILDRENPARENT.getNodeByName(-1))
    print(f'Total weight in CHILDRENPARENTS {pathCHILDRENPARENT.totalWeight}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')


    print('----------------------------File test_small.dag-------------------------')
    print('')
    firstGraphDFS = createGraph('test_small.dag', 'dfs')
    pathDFS = find(firstGraphDFS.getNodeByName(-2), firstGraphDFS, firstGraphDFS.getNodeByName(-1))
    print(f'Total weight in DFS {pathDFS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createGraph('test_small.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS.getNodeByName(-2), firstGraphDFSPLUS, firstGraphDFSPLUS.getNodeByName(-1))
    print(f'Total weight in DFS+ {pathDFSPLUS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createGraph('test_small.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN.getNodeByName(-2), firstGraphCHILDREN, firstGraphCHILDREN.getNodeByName(-1))
    print(f'Total weight in CHILDREN {pathCHILDREN.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createGraph('test_small.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT.getNodeByName(-2), firstGraphCHILDRENPARENT,
                              firstGraphCHILDRENPARENT.getNodeByName(-1))
    print(f'Total weight in CHILDRENPARENTS {pathCHILDRENPARENT.totalWeight}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_small_sparse.dag-------------------------')
    print('')
    firstGraphDFS = createGraph('test_small_sparse.dag', 'dfs')
    pathDFS = find(firstGraphDFS.getNodeByName(-2), firstGraphDFS, firstGraphDFS.getNodeByName(-1))
    print(f'Total weight in DFS {pathDFS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createGraph('test_small_sparse.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS.getNodeByName(-2), firstGraphDFSPLUS, firstGraphDFSPLUS.getNodeByName(-1))
    print(f'Total weight in DFS+ {pathDFSPLUS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createGraph('test_small_sparse.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN.getNodeByName(-2), firstGraphCHILDREN, firstGraphCHILDREN.getNodeByName(-1))
    print(f'Total weight in CHILDREN {pathCHILDREN.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createGraph('test_small_sparse.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT.getNodeByName(-2), firstGraphCHILDRENPARENT,
                              firstGraphCHILDRENPARENT.getNodeByName(-1))
    print(f'Total weight in CHILDRENPARENTS {pathCHILDRENPARENT.totalWeight}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_medium.dag-------------------------')
    print('')
    firstGraphDFS = createGraph('test_medium.dag', 'dfs')
    pathDFS = find(firstGraphDFS.getNodeByName(-2), firstGraphDFS, firstGraphDFS.getNodeByName(-1))
    print(f'Total weight in DFS {pathDFS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createGraph('test_medium.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS.getNodeByName(-2), firstGraphDFSPLUS, firstGraphDFSPLUS.getNodeByName(-1))
    print(f'Total weight in DFS+ {pathDFSPLUS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createGraph('test_medium.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN.getNodeByName(-2), firstGraphCHILDREN, firstGraphCHILDREN.getNodeByName(-1))
    print(f'Total weight in CHILDREN {pathCHILDREN.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createGraph('test_medium.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT.getNodeByName(-2), firstGraphCHILDRENPARENT,
                              firstGraphCHILDRENPARENT.getNodeByName(-1))
    print(f'Total weight in CHILDRENPARENTS {pathCHILDRENPARENT.totalWeight}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_medium_sparse.dag-------------------------')
    print('')
    firstGraphDFS = createGraph('test_medium_sparse.dag', 'dfs')
    pathDFS = find(firstGraphDFS.getNodeByName(-2), firstGraphDFS, firstGraphDFS.getNodeByName(-1))
    print(f'Total weight in DFS {pathDFS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createGraph('test_medium_sparse.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS.getNodeByName(-2), firstGraphDFSPLUS, firstGraphDFSPLUS.getNodeByName(-1))
    print(f'Total weight in DFS+ {pathDFSPLUS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createGraph('test_medium_sparse.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN.getNodeByName(-2), firstGraphCHILDREN, firstGraphCHILDREN.getNodeByName(-1))
    print(f'Total weight in CHILDREN {pathCHILDREN.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createGraph('test_medium_sparse.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT.getNodeByName(-2), firstGraphCHILDRENPARENT,
                              firstGraphCHILDRENPARENT.getNodeByName(-1))
    print(f'Total weight in CHILDRENPARENTS {pathCHILDRENPARENT.totalWeight}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_large.dag-------------------------')
    print('')
    firstGraphDFS = createGraph('test_large.dag', 'dfs')
    pathDFS = find(firstGraphDFS.getNodeByName(-2), firstGraphDFS, firstGraphDFS.getNodeByName(-1))
    print(f'Total weight in DFS {pathDFS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createGraph('test_large.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS.getNodeByName(-2), firstGraphDFSPLUS, firstGraphDFSPLUS.getNodeByName(-1))
    print(f'Total weight in DFS+ {pathDFSPLUS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createGraph('test_large.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN.getNodeByName(-2), firstGraphCHILDREN, firstGraphCHILDREN.getNodeByName(-1))
    print(f'Total weight in CHILDREN {pathCHILDREN.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createGraph('test_large.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT.getNodeByName(-2), firstGraphCHILDRENPARENT,
                              firstGraphCHILDRENPARENT.getNodeByName(-1))
    print(f'Total weight in CHILDRENPARENTS {pathCHILDRENPARENT.totalWeight}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_large_sparse.dag-------------------------')
    print('')
    firstGraphDFS = createGraph('test_large_sparse.dag', 'dfs')
    pathDFS = find(firstGraphDFS.getNodeByName(-2), firstGraphDFS, firstGraphDFS.getNodeByName(-1))
    print(f'Total weight in DFS {pathDFS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createGraph('test_large_sparse.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS.getNodeByName(-2), firstGraphDFSPLUS, firstGraphDFSPLUS.getNodeByName(-1))
    print(f'Total weight in DFS+ {pathDFSPLUS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createGraph('test_large_sparse.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN.getNodeByName(-2), firstGraphCHILDREN, firstGraphCHILDREN.getNodeByName(-1))
    print(f'Total weight in CHILDREN {pathCHILDREN.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createGraph('test_large_sparse.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT.getNodeByName(-2), firstGraphCHILDRENPARENT,
                              firstGraphCHILDRENPARENT.getNodeByName(-1))
    print(f'Total weight in CHILDRENPARENTS {pathCHILDRENPARENT.totalWeight}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_xlarge_sparse.dag-------------------------')
    print('')
    firstGraphDFS = createGraph('test_xlarge_sparse.dag', 'dfs')
    pathDFS = find(firstGraphDFS.getNodeByName(-2), firstGraphDFS, firstGraphDFS.getNodeByName(-1))
    print(f'Total weight in DFS {pathDFS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createGraph('test_xlarge_sparse.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS.getNodeByName(-2), firstGraphDFSPLUS, firstGraphDFSPLUS.getNodeByName(-1))
    print(f'Total weight in DFS+ {pathDFSPLUS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createGraph('test_xlarge_sparse.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN.getNodeByName(-2), firstGraphCHILDREN, firstGraphCHILDREN.getNodeByName(-1))
    print(f'Total weight in CHILDREN {pathCHILDREN.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createGraph('test_xlarge_sparse.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT.getNodeByName(-2), firstGraphCHILDRENPARENT,
                              firstGraphCHILDRENPARENT.getNodeByName(-1))
    print(f'Total weight in CHILDRENPARENTS {pathCHILDRENPARENT.totalWeight}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_xlarge.dag-------------------------')
    print('')
    firstGraphDFS = createGraph('test_xlarge.dag', 'dfs')
    pathDFS = find(firstGraphDFS.getNodeByName(-2), firstGraphDFS, firstGraphDFS.getNodeByName(-1))
    print(f'Total weight in DFS {pathDFS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createGraph('test_xlarge.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS.getNodeByName(-2), firstGraphDFSPLUS, firstGraphDFSPLUS.getNodeByName(-1))
    print(f'Total weight in DFS+ {pathDFSPLUS.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createGraph('test_xlarge.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN.getNodeByName(-2), firstGraphCHILDREN, firstGraphCHILDREN.getNodeByName(-1))
    print(f'Total weight in CHILDREN {pathCHILDREN.totalWeight}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createGraph('test_xlarge.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT.getNodeByName(-2), firstGraphCHILDRENPARENT,
                              firstGraphCHILDRENPARENT.getNodeByName(-1))
    print(f'Total weight in CHILDRENPARENTS {pathCHILDRENPARENT.totalWeight}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
