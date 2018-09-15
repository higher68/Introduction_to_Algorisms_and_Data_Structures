# 要請は双方向連結だけど、実装しんどいので、ひとまず連結リストから実装
# 連結リストで実装する場合、
# 順番にinputをロードしてくかな。

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
        def __init__(self, data, link=None):
            self.data = data
            self.link = link

    def __init__(self, *args):
        self.top = Linkedlist.Cell(None)  # ダミー。何も入ってないセル。なぜ作るんだろう
        for x in reversed(args):  # 後ろから辿っていき、先頭に順番に追加。argsと同じ順番で要素を並べられる。
            print("hogeeee")  # Linkedlistの引数に最初に何も入れなかったら入らないループ
            self.insert(0, x)

    def nth(self, n):
        '''
        n番目のセルを探索する
        return
        n番目のセルのオブジェクト
        '''
        i = -1  # ダミーのセルから探索開始
        cp = self.top
        # print("hoge1", n)
        while cp is not None:
            # print("hoge2", n)
            if i == n:
                return cp  # n番目のセルに当たったら終了
            i += 1  # セルの番号を次に
            cp = cp.link  # 次のセルに移動
        # print("hoge3") リストの番号を1から始めようとすると、
        # ダミーセルが-1ばんめなので、0番目がNone になり
        # 追加されないで終わる
        return None  # 例外処理。セルがn個なかったらNone

    def at(self, n):
        '''
        n番目のセルの値を返す
        return
        n番目のセルの保有する値
        '''
        cp = self.nth(n)
        if cp is not None:  # 値を持ってたら返す。なければNone
            return cp.data
        return None

    def insert(self, n, x):
        '''
        n番目にセルを挿入。
        内部操作としては、n-1番目のセルを特定、
        新しいセルオブジェクトを生成
        データと元々のn番目へのリンクを格納
        return
        挿入したデータ
        '''
        cp = self.nth(n-1)
        if cp is not None:
            cp.link = Linkedlist.Cell(x, cp.link)
            return x
        return None

    def delete(self, n):
        '''
        n番目のセルを削除。
        操作としては、n-1番目のセルと、n+1番目のセルが存在している時に
        n-1番目のセルのリンクをn+1番目へのリンクに貼り直す
        return
        削除したセルに格納されていたデータ
        '''
        cp = self.nth(n-1)
        if cp is not None and cp.link is not None:
            data = cp.link.data
            cp.link = cp.link.link
            return data  # 削除したセルのデータを出力


# 連結リストの初期化
a = Linkedlist()
right_end = -1
for i in range(n):
    if len(q[i]) == 2:
        if q[i][0] == "insert":
            a.insert(0, q[i][1])
            # print(a.at(index))
            # exit()
            right_end += 1
            # print("insert i:{} right_end:{}".format(i, right_end))
            # for k in range(right_end+1):
            #     print(a.at(k))
        elif q[i][0] == "delete":
            for j in range(right_end+1):  # ここがO(N)の原因
                if a.at(j) == q[i][1]:
                    a.delete(j)
                    right_end -= 1
                    # print("delete i:{} right_end:{}".format(i, right_end))

                    # for k in range(right_end+1):
                    #     print(a.at(k))
                    break
    else:
        if q[i] == "deleteFirst":
            a.delete(0)
            right_end -= 1
            # print("deleteFirst i:{} right_end:{}".format(i, right_end))
            # for k in range(right_end+1):
            #     print(a.at(k))
        elif q[i] == "deleteLast":
            a.delete(right_end)
            right_end -= 1
            # print("deleteLast i:{} right_end:{}".format(i, right_end))
            # for k in range(right_end+1):
            #     print(a.at(k))

for i in range(right_end):
    print(a.at(i), end=" ")
print(a.at(right_end))
