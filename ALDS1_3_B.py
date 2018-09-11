n, q = map(int, input().split())
p = []
for i in range(n):
    p_tmp = input().split()
    p.append([p_tmp[0], int(p_tmp[1])])
print(n, q)
for i in range(n):
    print(i, p[i])
