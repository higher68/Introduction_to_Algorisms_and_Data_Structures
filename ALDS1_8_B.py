class Node:
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right


def insert():


def inorder(node_k):
    if


def preorder():



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
