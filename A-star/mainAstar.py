from Node import Node
import time

def createNodeFile(fileName,str):
    with open(fileName) as f:
        lines = f.readlines()
    count = 0
    index = 0
    index2 = 0
    for line in lines:
        count += 1

        if count == 1:
            numNodes = int(line)
            graphL = []
            for i in range(numNodes):
                newNode = Node()
                newNode.number = i
                graphL.append(newNode)

        if count < numNodes + 2 and count > 1:
            graphL[index2].weight = float(line)
            index2 += 1

        if count >= numNodes + 2:
            numList = list(line.split(" "))
            ints = []
            if numList[0] != -1:
                for element in numList:
                    for node in graphL:
                        if node.number == int(element):
                            ints.append(node)
                graphL[index].addSuccessors(ints)
            index += 1

    startList = startingPoint(graphL)
    startNode = Node()
    startNode.weight = 0.0
    startNode.number = -100
    finalNode = Node()
    finalNode.weight = 0.0
    finalNode.number = -1
    startNode.addSuccessors(startList)

    graphL.append(startNode)
    graphL.append(finalNode)
    addFinalNode(graphL, graphL[-1])
    getParents(graphL)

    if str is 'children':
        start = time.time_ns()
        childHeuristics(graphL)
        finish = time.time_ns()
        timeFIN = finish - start
        print(f' time of heuristics calculation for Children is in nanoSec:')
        print("%.20f" % timeFIN)
    if str is 'dfs':
        start = time.time_ns()
        DFSheuristics(graphL)
        finish = time.time_ns()
        timeFIN = finish - start
        print(f' time of heuristics calculation for DFS is in nanoSec:')
        print("%.20f" % timeFIN)

    if str is "dfs+":
        start = time.time_ns()
        DFSPLUSheuristics(graphL)
        finish = time.time_ns()
        timeFIN = finish - start
        print(f' time of heuristics calculation for DFS+ is in nanoSec:')
        print("%.20f" % timeFIN)
    if str is "childrenparent":
        start = time.time_ns()
        childParentHeuristics(graphL)
        finish = time.time_ns()
        timeFIN = finish - start
        print(f' time of heuristics calculation for Children&parents  is in nanoSec:')
        print("%.20f" % timeFIN)

    return graphL


def startingPoint(listN: [Node]):
    startL = []
    for elem in listN:
        isParent = True
        for inListElement in listN:
            successors = inListElement.successors
            if elem in successors:
                isParent = False
        if isParent == True:
            startL.append(elem)

    return startL

def addFinalNode(nodeList: [Node], node: Node):
    listname = []
    listname.append(node)
    for elem in nodeList:
        children = elem.successors
        if len(children) == 0:
            elem.addSuccessors(listname)

def getParents(nodeList:[Node]):
    for elem in nodeList:
        for inListElement in nodeList:
            num = elem.number
            successors = inListElement.successors
            if num in successors:
                elem.predecessors.append(inListElement)


def find(node: Node, finalNode: Node):
    unvisited = []
    visited = []
    node.g = node.weight
    unvisited.append(node)

    while len(unvisited) != 0:
        unvisited.sort(key=lambda x: x.f, reverse=True)
        curNode = unvisited[0]
        ind = 0
        unvisited.pop(ind)

        if curNode is finalNode:
            path = []
            while curNode.parent != None:
                path.append(curNode)
                curNode = curNode.parent
            return path

        else:
            suc = curNode.successors
            for child in suc:
                candidateWeight = curNode.g + curNode.weight
                if candidateWeight >= child.g:
                    child.parent = curNode
                    visited.append(child)
                    child.g = candidateWeight
                    child.f = child.g + child.h
                    if child not in unvisited:
                        unvisited.append(child)

def DFS(visited, node):
    if node not in visited:
        visited.add(node)
        suc = node.successors
        for neighbour in suc:
            DFS(visited, neighbour)


def DFS_heuris(nodeList: [Node]):
    for elem in nodeList:
        visited = set()
        DFS(visited, elem)
        elem.h = len(visited)

def DFSheuristics(nodeList:[Node]):
    for elem in nodeList:
        visited=set()
        DFS(visited,elem)
        elem.h=len(visited)

def DFSPLUSheuristics(nodeList:[Node]):
    for elem in nodeList:
        visited=set()
        dfs(visited,elem)
        elem.h=len(visited)+elem.weight

def childParentHeuristics(nodeList:[Node]):
    for elem in nodeList:
        elem.h=len(elem.predecessors)+len(elem.successors)



def childHeuristics(nodeList:[Node]):
    for elem in nodeList:
        hValue = 0
        children = elem.successors
        if len(children) is not 0:
            for i in children:
                hValue =hValue+  i.weight
            # hValue = hValue / len(children)
        hValue+=elem.weight
        elem.h = hValue

def totalWeight(nodeList:[Node]):
    sum=0
    for elem in nodeList:
        sum += elem.weight
    return sum




if __name__ == '__main__':


    print('----------------------------File test.txt-------------------------')
    print('')
    firstGraphDFS = createNodeFile('test.txt', 'dfs')
    pathDFS = find(firstGraphDFS[-2],firstGraphDFS[-1])
    print(f'Total weight in DFS {totalWeight(pathDFS)}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createNodeFile('test.txt', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS[-2],firstGraphDFSPLUS[-1])
    print(f'Total weight in DFS+ {totalWeight(pathDFSPLUS)}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createNodeFile('test.txt', 'children')
    pathCHILDREN = find(firstGraphCHILDREN[-2],firstGraphCHILDREN[-1])
    print(f'Total weight in CHILDREN {totalWeight(pathCHILDREN)}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createNodeFile('test.txt', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT[-2],
                              firstGraphCHILDRENPARENT[-1])
    print(f'Total weight in CHILDRENPARENTS {totalWeight(pathCHILDRENPARENT)}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_small.dag-------------------------')
    print('')
    firstGraphDFS = createNodeFile('test_small.dag', 'dfs')
    pathDFS = find(firstGraphDFS[-2],  firstGraphDFS[-1])
    print(f'Total weight in DFS {totalWeight(pathDFS)}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createNodeFile('test_small.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS[-2],firstGraphDFSPLUS[-1])
    print(f'Total weight in DFS+ {totalWeight(pathDFSPLUS)}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createNodeFile('test_small.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN[-2],firstGraphCHILDREN[-1])
    print(f'Total weight in CHILDREN {totalWeight(pathCHILDREN)}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createNodeFile('test_small.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT[-2],
                              firstGraphCHILDRENPARENT[-1])
    print(f'Total weight in CHILDRENPARENTS {totalWeight(pathCHILDRENPARENT)}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_small_sparse.dag-------------------------')
    print('')
    firstGraphDFS = createNodeFile('test_small_sparse.dag', 'dfs')
    pathDFS = find(firstGraphDFS[-2],  firstGraphDFS[-1])
    print(f'Total weight in DFS {totalWeight(pathDFS)}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createNodeFile('test_small_sparse.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS[-2],firstGraphDFSPLUS[-1])
    print(f'Total weight in DFS+ {totalWeight(pathDFSPLUS)}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createNodeFile('test_small_sparse.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN[-2],firstGraphCHILDREN[-1])
    print(f'Total weight in CHILDREN {totalWeight(pathCHILDREN)}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createNodeFile('test_small_sparse.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT[-2],
                              firstGraphCHILDRENPARENT[-1])
    print(f'Total weight in CHILDRENPARENTS {totalWeight(pathCHILDRENPARENT)}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_medium.dag-------------------------')
    print('')
    firstGraphDFS = createNodeFile('test_medium.dag', 'dfs')
    pathDFS = find(firstGraphDFS[-2],firstGraphDFS[-1])
    print(f'Total weight in DFS {totalWeight(pathDFS)}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createNodeFile('test_medium.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS[-2], firstGraphDFSPLUS[-1])
    print(f'Total weight in DFS+ {totalWeight(pathDFSPLUS)}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createNodeFile('test_medium.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN[-2], firstGraphCHILDREN[-1])
    print(f'Total weight in CHILDREN {totalWeight(pathCHILDREN)}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createNodeFile('test_medium.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT[-2],
                              firstGraphCHILDRENPARENT[-1])
    print(f'Total weight in CHILDRENPARENTS {totalWeight(pathCHILDRENPARENT)}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_medium_sparse.dag-------------------------')
    print('')
    firstGraphDFS =createNodeFile('test_medium_sparse.dag', 'dfs')
    pathDFS = find(firstGraphDFS[-2], firstGraphDFS[-1])
    print(f'Total weight in DFS {totalWeight(pathDFS)}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createNodeFile('test_medium_sparse.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS[-2], firstGraphDFSPLUS[-1])
    print(f'Total weight in DFS+ {totalWeight(pathDFSPLUS)}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createNodeFile('test_medium_sparse.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN[-2], firstGraphCHILDREN[-1])
    print(f'Total weight in CHILDREN {totalWeight(pathCHILDREN)}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createNodeFile('test_medium_sparse.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT[-2], firstGraphCHILDRENPARENT[-1])
    print(f'Total weight in CHILDRENPARENTS {totalWeight(pathCHILDRENPARENT)}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_large.dag-------------------------')
    print('')
    firstGraphDFS = createNodeFile('test_large.dag', 'dfs')
    pathDFS = find(firstGraphDFS[-2], firstGraphDFS[-1])
    print(f'Total weight in DFS {totalWeight(pathDFS)}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createNodeFile('test_large.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS[-2], firstGraphDFSPLUS[-1])
    print(f'Total weight in DFS+ {totalWeight(pathDFSPLUS)}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createNodeFile('test_large.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN[-2], firstGraphCHILDREN[-1])
    print(f'Total weight in CHILDREN {totalWeight(pathCHILDREN)}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createNodeFile('test_large.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT[-2], firstGraphCHILDRENPARENT[-1])
    print(f'Total weight in CHILDRENPARENTS {totalWeight(pathCHILDRENPARENT)}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_large_sparse.dag-------------------------')
    print('')
    firstGraphDFS = createNodeFile('test_large_sparse.dag', 'dfs')
    pathDFS = find(firstGraphDFS[-2], firstGraphDFS[-1])
    print(f'Total weight in DFS {totalWeight(pathDFS)}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createNodeFile('test_large_sparse.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS[-2], firstGraphDFSPLUS[-1])
    print(f'Total weight in DFS+ {totalWeight(pathDFSPLUS)}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createNodeFile('test_large_sparse.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN[-2], firstGraphCHILDREN[-1])
    print(f'Total weight in CHILDREN {totalWeight(pathCHILDREN)}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createNodeFile('test_large_sparse.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT[-2], firstGraphCHILDRENPARENT[-1])
    print(f'Total weight in CHILDRENPARENTS {totalWeight(pathCHILDRENPARENT)}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_xlarge_sparse.dag-------------------------')
    print('')
    firstGraphDFS = createNodeFile('test_xlarge_sparse.dag', 'dfs')
    pathDFS = find(firstGraphDFS[-2], firstGraphDFS[-1])
    print(f'Total weight in DFS {totalWeight(pathDFS)}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS = createNodeFile('test_xlarge_sparse.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS[-2], firstGraphDFSPLUS[-1])
    print(f'Total weight in DFS+ {totalWeight(pathDFSPLUS)}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createNodeFile('test_xlarge_sparse.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN[-2], firstGraphCHILDREN[-1])
    print(f'Total weight in CHILDREN {totalWeight(pathCHILDREN)}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createNodeFile('test_xlarge_sparse.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT[-2], firstGraphCHILDRENPARENT[-1])
    print(f'Total weight in CHILDRENPARENTS {totalWeight(pathCHILDRENPARENT)}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

    print('----------------------------File test_xlarge.dag-------------------------')
    print('')
    firstGraphDFS = createNodeFile('test_xlarge.dag', 'dfs')
    pathDFS = find(firstGraphDFS[-2], firstGraphDFS[-1])
    print(f'Total weight in DFS {totalWeight(pathDFS)}')
    print('---------------------------------------------------')
    firstGraphDFSPLUS =createNodeFile('test_xlarge.dag', 'dfs+')
    pathDFSPLUS = find(firstGraphDFSPLUS[-2], firstGraphDFSPLUS[-1])
    print(f'Total weight in DFS+ {totalWeight(pathDFSPLUS)}')
    print('---------------------------------------------------')
    firstGraphCHILDREN = createNodeFile('test_xlarge.dag', 'children')
    pathCHILDREN = find(firstGraphCHILDREN[-2], firstGraphCHILDREN[-1])
    print(f'Total weight in CHILDREN {totalWeight(pathCHILDREN)}')
    print('---------------------------------------------------')
    firstGraphCHILDRENPARENT = createNodeFile('test_xlarge.dag', 'childrenparent')
    pathCHILDRENPARENT = find(firstGraphCHILDRENPARENT[-2], firstGraphCHILDRENPARENT[-1])
    print(f'Total weight in CHILDRENPARENTS {totalWeight(pathCHILDRENPARENT)}')
    print('---------------------------------------------------')
    print('---------------------------------------------------')

