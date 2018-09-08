n = int(input())
a = [int(_) for _ in input().split()]
for i in range(n-1):
    print(a[i], end=" ")
print(a[n-1])
for i in range(1, n):
    insert = a[i]
    # print('i', i)

    for j in range(i-1, -1, -1):
        # print('j', j)
        if a[j] > insert:
            a[j+1] = a[j]
            a[j] = insert
        else:
            break
    for i in range(n-1):
        print(a[i], end=" ")
    print(a[n-1])
