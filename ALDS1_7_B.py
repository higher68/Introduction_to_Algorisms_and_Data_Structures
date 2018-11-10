class Node:
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right


n = int(input())
Nodes = [Node()] * n
# input Node-info
for i in range(n):
    q = [int(_) for _ in input().split()]
    if q[1] != -1:
         Nodes[i].left = q[1]
    if q[2] != -1:
        Nodes[i].right = q[2]
