n = int(input())
a = [int(_) for _ in input().split()]
neighbor = True
change_count = 0
while neighbor:
    neighbor = False
    for i in range(n-1, 0, -1):
        if a[i] < a[i-1]:
            change_count += 1
            a_tmp = a[i]
            a[i] = a[i-1]
            a[i-1] = a_tmp
            neighbor = True
for i in range(n-1):
    print(a[i], end=" ")
print(a[n-1])
print(change_count)
