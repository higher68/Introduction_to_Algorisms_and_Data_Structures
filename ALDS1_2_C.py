import copy
n = int(input())
a = input().split()
a_sr = []
a_sr_l = []
for i in range(n-1):
    if a[i][1] not in a_sr_l:
        for j in range(i+1, n):
            if a[i][1] == a[j][1]:
                if a[i][1] not in a_sr_l:
                    a_sr_l.append(a[i][1])
                if len(a_sr) == 0:
                    a_sr.append(a[i][0])
                a_sr.append(a[j][0])
a_b = copy.deepcopy(a)
a_s = copy.deepcopy(a)
# print(a)
# print(a1)
# print(a2)

# Bubble Sort
neighbor = True
while neighbor:
    neighbor = False
    for i in range(n-1, 0, -1):
        if a_b[i][1] < a_b[i-1][1]:
            a_tmp = a_b[i]
            a_b[i] = a_b[i-1]
            a_b[i-1] = a_tmp
            neighbor = True
for i in range(n-1):
    print(a_b[i], end=" ")
print(a_b[n-1])
a_b_s = []
a_b_s_l = []
for _ in a_sr_l:
    for i in range(n):
        if a_b[i][1] == _ and _ not in a_b_s_l:
            for j in range(i+1, n):
                if a_b[i][1] == a_b[j][1]:
                    if a_b[i][1] not in a_b_s_l:
                        a_b_s_l.append(a_b[i][1])
                    if len(a_b_s) == 0:
                        a_b_s.append(a_b[i][0])
                    a_b_s.append(a_b[j][0])

if a_b_s != a_sr:
    print("Not stable")
else:
    print("Stable")
# Selection Sort
# print(a_s)
for i in range(n-1):
    tmp_index = i
    for j in range(i+1, n):
        # 最小の値探索
        # print("# temp", tmp_index, "j", j)
        if a_s[j][1] < a_s[tmp_index][1]:
            tmp_index = j
    if tmp_index != i:
        # 最小と左端入れ替え
        a_tmp = a_s[i]
        a_s[i] = a_s[tmp_index]
        a_s[tmp_index] = a_tmp
for i in range(n-1):
    print(a_s[i], end=" ")
print(a_s[n-1])
a_s_s = []
a_s_s_l = []
for _ in a_sr_l:
    for i in range(n):
        if a_s[i][1] == _ and _ not in a_s_s_l:
            for j in range(i+1, n):
                if a_s[i][1] == a_s[j][1]:
                    if a_s[i][1] not in a_s_s_l:
                        a_s_s_l.append(a_s[i][1])
                    if len(a_s_s) == 0:
                        a_s_s.append(a_s[i][0])
                    a_s_s.append(a_s[j][0])
# print("a_s_s", a_s_s)
# print("a_sr", a_sr)
if a_s_s != a_sr:
    print("Not stable")
else:
    print("Stable")
