class Node:
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right


def PrintNodes(i):
    print("node {}: ".formt(i), end="")
    print("parent = {}, ".formt())
    else:



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
