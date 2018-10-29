#  ouput:parent, depth, type, 子の節点番号をそれぞれのノードに対してアウトプット

class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

def getDepth(u):
    '''
    depthを入力した番号のノードに対して求める
    '''
    d = 0
    while Nodes[u].parent != NULL:
        u = Nodes[u].parent
        d += 1
    return d


def printChild(u):
    c = Nodes[u].left
    while c != NULL:
        print(c)
        c = Nodes[c]

def printNode(u):
    print()



n = int(input())

Nodes = [""] * n
