n = int(input())
r = []
for i in range(n):
    r.append(int(input()))
min = r[0]
max_prof = -2000000000000
for i in range(1, n):
    if (r[i] - min) > max_prof:
        max_prof = r[i] - min
    if r[i] < min:
        min = r[i]
print(max_prof)
