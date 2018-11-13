class Node:
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right


def PrintNodes(i):
    print("node {}: ".format(i), end="")
    print("parent = {}, ".format(Nodes[i].parent))
    if Nodes[Nodes[i].parent].left == i:
        if Nodes[Nodes[i].parent].right is not None:
            print("sibling = {}, ".format(Nodes[Nodes[i].parent].right))
        else:
            print("sibling = {}, ".format(-1))
    elif Nodes[Nodes[i].parent].right == i:
        if Nodes[Nodes[i].parent].left is not None:
            print("sibling = {}, ".format(Nodes[Nodes[i].parent].left))
        else:
            print("sibling = {}, ".format(-1))
    deg = 0
    if Nodes[i].left is not None:
        deg += 1
    if Nodes[i].right is not None:
        deg += 1
    print("depth = {}, ".format(deg))
    if Nodes[i].parent == 1:
        print("root")
    else:
        if deg != 0:
            print("internal node")
        else:
            print("leaf")





def recur(i_node, depth):
    Depth[i_node] = depth
    if Depth[i_node].left is not None:
        recur(Depth[i_node].left, depth+1)
    if Depth[i_node].right is not None:
        recur(Depth[i_node].right, depth+1)


n = int(input())
Depth = [""] * n
Nodes = [Node()] * n
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
for i in range(n):
    if Nodes[i].parent is None:
        Nodes[i].parent = -1
        rooot_node = i
        break

recur(r, 0)
