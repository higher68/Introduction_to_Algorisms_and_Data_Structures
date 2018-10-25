def partition(p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A_tmp = A[i]
            A[i] = A[j]
            A[j] = A_tmp
        t = A[i+1]
        A[i+1] = A[r]
        A[r] = t


n = int(input())
A = [int(_) for _ in input().split()]
q = partition(0, n-1)
for i in range(n):
    if i:
        print(" ")
    if i == q:
        print("[")
    print(A[i])
    if i == q:
        print("]")
print("\n")
