n = int(input())
a = [int(_) for _ in input().split()]
count = 0
for i in range(n-1):
    tmp_index = i
    for j in range(i+1, n):
        # 最小の値探索
        # print("# temp", tmp_index, "j", j)
        if a[j] < a[tmp_index]:
            tmp_index = j
    if tmp_index != i:
        count += 1
        # 最小と左端入れ替え
        a_tmp = a[i]
        a[i] = a[tmp_index]
        a[tmp_index] = a_tmp
for i in range(n-1):
    print(a[i], end=" ")
print(a[n-1])
print(count)
