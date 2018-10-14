n = int(input())
a = [int(_) for _ in input().split()]
q = int(input())
m = [int(_) for _ in input().split()]


def solve(i, m1):
    if m1 == 0:
        return True
    if i >= n:  # 探索範囲を超えた時
        return False
    # 下記二つのいずれかがTrueの時、約数が存在
    res = solve(i+1, m1) or solve(i+1, m1-a[i])
    return res


for i in range(q):
    if solve(0, m[i]):
        print("yes")
    else:
        print("no")
