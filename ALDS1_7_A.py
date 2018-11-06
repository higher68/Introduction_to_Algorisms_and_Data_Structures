# ouput:parent, depth, type, 子の節点番号をそれぞれのノードに対してアウトプット
# pythonはnullじゃなくてNonce


class Node:
    '''
    leftは子ノード
    rightは同depthのノード
    '''
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None


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
    print("node {}:".format(u), end="")
    print("parent = {}, ".format(Nodes[u].parent), end="")
    print("depth = {}, ".format(Depth[u]), end="")
    if Nodes[u].parent == -1:
        print("root, ", end="")
    elif Nodes[u].left is None:
        print("leaf, ", end="")
    else:
        print("internal node", end="")
    print("[", end="")
    c = Nodes[u].left
    i = 0
    while c is not None:
        if i == 0:
            print("{}".format(c), end="")
        else:
            print(", {}".format(c), end="")
        c = Nodes[c].right
        i += 1
        if i == 5:
            exit()
    print("]")


def rec(u, p):
    Depth[u] = p
    if Nodes[u].right is not None:
        rec(Nodes[u].right, p)
    if Nodes[u].left is not None:
        rec(Nodes[u].right, p)


n = int(input())
# print(n)


Nodes = [[] for i in range(n)]
for i in range(n):
    Nodes[i] = Node()  # classを宣言するときは、()がないとおかしなことになる
# print(type(Nodes))
# print("len", len(Nodes))
# for i in range(n):
#     Nodes[i].left, Nodes[i].right, Nodes[i].parent = i, i, i
# for i in range(n):
#     print(i, Nodes[i].left, Nodes[i].right, Nodes[i].parent)
# exit()
Depth = [""] * n
# for i in range(n):
#     print(i, Nodes[i].parent, Nodes[i].left, Nodes[i].right)
#     Nodes[i].parent, Nodes[i].left, Nodes[i].right = 1, 1, 1
#     print(i, Nodes[i].parent, Nodes[i].left, Nodes[i].right)
# exit()
for i in range(n):
    q_in = [int(_) for _ in input().split()]
    # print(q_in)
    Node_number = q_in[0]
    dimention = q_in[1]
    # print(Node_number, dimention)
    if dimention > 2:
        for j in range(0, dimention):
            # print(j, '-'*20)
            # print('hoge', j+2, q_in[j+2], Node_number)
            if j == 0:
                Nodes[Node_number].left = q_in[j+2]
            else:
                Nodes[Node_number].right = q_in[j+2]
            # print(type(Nodes[q_in[j+2]].parent))
            if Node_number == 0:
                # print("Node_number1", Node_number, q_in[j+2])
                Nodes[0].parent = -1
            else:
                # print("Node_number2", Node_number, q_in[j+2])
                # print("Nodes[q_in[j+2]].parent, Nodes[0].parent", Nodes[q_in[j+2]].parent, Nodes[0].parent)
                Nodes[q_in[j+2]].parent = Node_number
            # print("Nodes[0].left, Nodes[0].parent, Nodes[0].right", Nodes[0].left,
            # Nodes[0].parent, Nodes[0].right)
            Node_number = q_in[j+2]
    # print("Nodes[0].left, Nodes[0].parent, Nodes[0].right", Nodes[0].left, Nodes[0].parent, Nodes[0].right)
    # exit()
    # print("hoge")
    # exit()
# exit()
r = -11
for i in range(n):
    if Nodes[i].parent is None:
        r = i
        break
if r != -11:
    rec(r, 0)

for i in range(n):
    printNode(i)
