# 要請は双方向連結だけど、実装しんどいので、ひとまず連結リストから実装
n = int(input())
q_tmp = [input().split() for i in range(n)]
q = []
for i in range(n):
    if len(q_tmp[i]) > 1:
        q.append([q_tmp[i][0], q_tmp[i][1]])
    else:
        q.append(q_tmp[i][0])
ans = []
class Linkedlist:
    # データの実体とポインタを内包したCellの実装
    class Cell:
        def __init__(self, x, y=None):
            self.data = x
            self.next = y
    ##
    def __init__(self *args):
        self.top = Linkedlist.Cell(None)  # ダミー。何も入ってないセル。なぜ作るんだろう
        for x in reversed(args):  # 後ろから辿っていき、先頭に順番に追加。argsと同じ順番で要素を並べられる。
            self.insert(0, x)
