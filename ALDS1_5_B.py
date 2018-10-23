
SENTINEL = 2000000000
n = int(input())
MAX = 500000
A_tmp = input().split()
print(A_tmp)
A = [''] * MAX
print(A[0:3])
for i in range(n):
    A[i] = int(A_tmp[i])
L = ['']*(MAX//2+2)
R = ['']*(MAX//2+2)
cnt = 0


def merge(A, n, left, mid, right):
    global cnt
    n1 = mid - left
    n2 = right - mid
    for i in range(n1):
        L[i] = A[left + i]
    for i in range(n2):
        R[i] = A[mid + i]
    L[n1] = SENTINEL
    R[n2] = SENTINEL
    i = 0
    j = 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[i]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, n, left, right):
    if left+1 < right:
        mid = (left+right)//2
        mergeSort(A, n, left, mid)
        mergeSort(A, n, mid, right)
        merge(A, n, left, mid, right)


mergeSort(A, n, 0, n)

print(A[:n], sep=" ")
print(cnt)
