# 双方向連結リスト実装

n = int(input())
q_tmp = [input().split() for i in range(n)]
q = []
for i in range(n):
    if len(q_tmp[i]) > 1:
        q.append([q_tmp[i][0], q_tmp[i][1]])
    else:
        q.append(q_tmp[i][0])
ans = []


class Deque:
    class Node:
        def __init__(self, data, x=None, y=None):
            self.data = data
            self.x = x
            self.y = y

    def __init__(self):
        head = Deque.Node(None)  # ヘッダリストの情報
        head.x = head
        head.y = head
        self.size = 0  # サイズの初期化
        self.head = head

    def front(self, data, n):
        '''
        ヘッドの後ろ=リストの先頭に要素を追加
        return
        入力値
        '''
        head = self.head
        if self.size == 0:
            new_node = Deque.Node(data)
            head.x = new_node
            head.y = new_node
            new_node.x = head
            new_node.y = head
            self.size += 1
            return data
        else:
            new_node = Deque.Node(data)
            new_node.x = head
            new_node.y = head.y
            head.y = new_node
            self.size += 1
            return data
        return None

    def listSearch(self, data):
        '''
        先頭からリストを辿って、値に当たるまで探す
        return
        該当するノード
        '''
        current_node = self.head
        while current_node.data != data:
            current_node = current_node.y
            if current_node == self.head:
                return None
        return current_node

    def delete(self, target):
        '''
        listSearchで見つけたノードを削除する
        return
        削除したノードの持つ値
        '''
        if target != self.head:
            prev_node = target.x
            next_node = target.y
            prev_node.y = next_node
            next_node.x = prev_node
            self.size -= 1
            return target.data

    def deleteFirst(self):
        '''先頭のノードの削除
        return
        削除したノードの持つ値
        '''
        if self.size != 0:
            head = self.head
            target = head.y
            next_node = target.y
            head.y = next_node
            next_node.x = head
            self.size -= 1
            return target.data

    def deleteLast(self):
        ''' 末端のノードの削除
        return
        削除したノードの持つ値
        '''
        if self.size != 0:
            head = self.head
            target = head.x
            prev_node = target.x
            head.x = prev_node
            prev_node.y = head
            self.size -= 1
            return target.data
