n, q = map(int, input().split())
p = []
for i in range(n):
    p_tmp = input().split()
    p.append([p_tmp[0], int(p_tmp[1])])
# print(n, q)
# for i in range(n):
#     print(i, p[i])
time = 0
while len(p) != 0:
    process_time = q
    # print(time)
    # print(process_time)
    # print(p)
    if p[0][1] > q:
        p_tmp = p.pop(0)
        p.append([p_tmp[0], p_tmp[1]-q])
        time += process_time
        process_time = 0
    else:
        process_time -= p[0][1]
        time += p[0][1]
        print(p[0][0], time)
        p.pop(0)
