
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
        if L[i] <= R[j]:
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


def partition(p, r):
    x = A[r]
    i = p - 1  # <xの右端
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A_tmp = A[i]
            A[i] = A[j]
            A[j] = A_tmp
    t = A[i+1]
    A[i+1] = A[r]
    A[r] = t
    return i+1


def quickSort(A, n, p, r):
    if p < r:
        q = partition(p, r)
        quickSort(A, n, p, q-1)
        quickSort(A, n, q+1, r)


class new_list:
    def __init__(self, a1, a2):
        self.suit = a1
        self.value = a2


n = int(input())
for i in range(n):
    S_tmp = input().split()
A = []
B = []
for i in range(n):
    A.append(new_list(S_tmp[0], S_tmp[1]))
    B.append(new_list(S_tmp[0], S_tmp[1]))

L = [''] * (n//2+2)
R = [''] * (n//2+2)
SENTINEL = 2000000000
mergeSort(A, n, 0, n)
quickSort(B, n, 0, n)
