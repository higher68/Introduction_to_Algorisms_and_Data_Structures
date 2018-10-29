# ouput:parent, depth, type, 子の節点番号をそれぞれのノードに対してアウトプット
# pythonはnullじゃなくてNonce


class Node:
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right


def getDepth(u):
    '''
    depthを入力した番号のノードに対して求める
    '''
    d = 0
    while Nodes[u].parent is not None:
        u = Nodes[u].parent
        d += 1
    return d


def printChild(u):
    c = Nodes[u].left
    while c is not None:
        print(c)
        c = Nodes[c]


def printNode(u):
    print("node {}:".formate(u))
    print("parent = {}, ".formate(Nodes[u].parent))
    print("depth = {}, ".formate(Depth[u]))
    if Nodes[u].parent is None:
        print("root, ")
    elif Nodes[u].left is None:
        print("leaf, ")
    else:
        print("internal node")
    print("[")
    i = 0
    c = Nodes[u].left
    while c is not None:
        if i:
            print(", {}".format(c))
    print("]")


def rec(u, p):
    Depth[u] = p
    if Node[u].right is not None:
        rec(Nodes[u].right, p)
    if Nodes[u].left is not None:
        rec(Nodes[u].right, p)


n = int(input())

Nodes = [Node()] * n
Depth = [""] * n
for i in range(n):
    q_in = [int(_) for _ in input().split()]
    tmp_parent = q_in[1]
    for j in range(2, len(q_in)):
        
