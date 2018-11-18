class Node:
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right


def preParse(u):
    """先行順巡回"""
    if u == -1:
        return
    print(" {}".format(u))
    preParse(Nodes[u].left)
    preParse(Nodes[u].right)


def inParse(u):
    """中間順巡回"""
    if u == -1:
        return
    inParse(Nodes[u].left)
    print(" {}".format(u))
    inParse(Nodes[u].right)


def postParse(u):
    """後行順巡回"""
    if u == -1:
        return
    postParse(Nodes[u].left)
    postParse(Nodes[u].right)
    print(" {}".format(u))


n = int(input())
Nodes = []
for i in range(n):
    Nodes.append(Node())

for i in range(n):
    tmp = [int(_) for _ in input().split()]
    Nodes[i].left = tmp[1]
    Nodes[i].right = tmp[2]
    if tmp[1] != -1:
        Nodes[tmp[1]].parent = tmp[0]
    if tmp[2] != -1:
        Nodes[tmp[2]].parent = tmp[0]

for i in range(n):
    print(i, Nodes[i].parent, Nodes[i].left, Nodes[i].right)
exit()
root = -11
for i in range(n):
    if Nodes[i].parent == -1:
        root = [i]
        break


print("Preorder")
preParse(root)
print("Inorder")
inParse(root)
print("Postorder")
postParse(root)
