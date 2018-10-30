# ouput:parent, depth, type, 子の節点番号をそれぞれのノードに対してアウトプット
# pythonはnullじゃなくてNonce


class Node:
    '''
    leftは子ノード
    rightは同depthのノード
    '''
    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right


# def getDepth(u):
#     '''
#     depthを入力した番号のノードに対して求める
#     '''
#     d = 0
#     while Nodes[u].parent is not None:
#         u = Nodes[u].parent
#         d += 1
#     return d
#
#
# def printChild(u):
#     c = Nodes[u].left
#     while c is not None:
#         print(c)
#         c = Nodes[c]


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
    c = Nodes[u].left
    while c is not None:
        if i:
            print(", {}".format(c))
        c = Nodes[c].right
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
    Node_number = q_in[0]
    dimention = q_in[1]
    for j in range(2, dimention):
        if j == 0:
            Nodes[Node_number].left = q_in[j+2]
        else:
            Nodes[Node_number].right = q_in[j+2]
        Node_number = q_in[j+2]
        Node[q_in[j+2]].parent = Node_number

for i in range(n):
    if Node[i].parent is None:
        r = i
        break

rec(r, 0)

for i in range(n):
    printNode(i)
