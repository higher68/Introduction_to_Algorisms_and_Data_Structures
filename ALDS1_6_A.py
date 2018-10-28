n = int(input())
A = [int(_) for _ in input().split()]
len_C = max(A) + 1
C = [0] * (len_C)
B = [0] * n
# 各値のカウント
for i in range(n):
    C[A[i]] += 1
# カウントの和をとる
for i in range(1, len_C):
    C[i] += C[i-1]

for i in range(n, -1, -1):
    B[C[A[i]]] = A[i]
    C[A[i]] -= 1

for i in range(n-1):
    print(B[i], end='')
print(B[n-1])
