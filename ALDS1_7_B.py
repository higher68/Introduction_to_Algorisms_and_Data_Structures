class Node:
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right


def PrintNodes(i):
    print("node {}: ".format(i), end="")
    print("parent = {}, ".format(Nodes[i].parent), end="")
    if Nodes[i].parent == -1:
        print("sibling = {}, ".format(-1), end="")
    else:
        if Nodes[Nodes[i].parent].left == i:
            if Nodes[Nodes[i].parent].right != -1:
                print("sibling = {}, ".format(Nodes[Nodes[i].parent].right), end="")
            else:
                print("sibling = {}, ".format(-1), end="")
        elif Nodes[Nodes[i].parent].right == i:
            if Nodes[Nodes[i].parent].left != -1:
                print("sibling = {}, ".format(Nodes[Nodes[i].parent].left), end="")
            else:
                print("sibling = {}, ".format(-1), end="")
    deg = 0
    if Nodes[i].left != -1:
        deg += 1
    if Nodes[i].right != -1:
        deg += 1
    print("degree = {}, ".format(deg), end="")
    print("depth = {}, ".format(Depth[i]), end="")
    print("height = {}, ".format(Height[i]), end="")
    if Nodes[i].parent == -1:
        print("root")
    else:
        if deg != 0:
            print("internal node")
        else:
            print("leaf")


def rec_depth(i_node, depth):
    # print("i_node, depth", i_node, depth)
    Depth[i_node] = depth
    if Nodes[i_node].left != -1:
        rec_depth(Nodes[i_node].left, depth+1)
    if Nodes[i_node].right != -1:
        rec_depth(Nodes[i_node].right, depth+1)


def rec_height(i_node):
    # print("i_node, height", i_node, height)
    # Height[i_node] = height
    # if Nodes[i_node].left != -1:
    #     rec_height(Nodes[i_node].left, height-1)
    # if Nodes[i_node].right != -1:
    #     rec_height(Nodes[i_node].right, height-1)
    h1 = 0
    h2 = 0
    if Nodes[i_node].left != -1:
        h1 = rec_height(Nodes[i_node].left) + 1
    if Nodes[i_node].right != -1:
        h2 = rec_height(Nodes[i_node].right) + 1
    Height[i_node] = max(h1, h2)
    return Height[i_node]


n = int(input())
Depth = [""] * n
Height = [""] * n
# Nodes = [Node()] * nやっぱこう書くと、 Nodeが全部同じのになるみたい。意味不明
Nodes = []
for i in range(n):
    Nodes.append(Node())
# input Node-info
for i in range(n):
    q = [int(_) for _ in input().split()]
    if q[1] != -1:
        Nodes[i].left = q[1]
        Nodes[q[1]].parent = i
    if q[2] != -1:
        Nodes[i].right = q[2]
        Nodes[q[2]].parent = i
root_node = -11
# for i in range(n):
    # print(i, Nodes[i].parent)
for i in range(n):
    if Nodes[i].parent == -1:
        root_node = i
        break
# print("hoghoge")
rec_depth(root_node, 0)
rec_height(root_node)

for i in range(n):
    PrintNodes(i)
