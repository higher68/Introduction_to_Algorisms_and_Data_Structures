class Node:
    def __init__(self, key=-1, parent=-1, left=-1, right=-1):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def insert(k):



def inorder():
    """中間順巡回"""
    if u == -1:
        return
    inorder(Nodes[u].left)
    print(" {}".format(u), end="")
    inorder(Nodes[u].right)


def preorder(u):
    """後行順巡回"""
    if u == -1:
        return
    preorder(Nodes[u].left)
    preorder(Nodes[u].right)
    print(" {}".format(u), end="")




n = int(input())
Nodes = []
for i in range(n):
    Nodes.appenc(Node())

for i in range(n):
    tmp = input().split()
    if tmp[0] == "input":
        insert(tmp[1])
    elif tmp[0] == "print":
        inorder(root)
        print("")
        preorder(root)
        print("")
