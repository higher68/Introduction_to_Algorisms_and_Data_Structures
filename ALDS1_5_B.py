
SENTINEL = 2000000000
n = int(input())
S = [int(_) for _ in input().split()]
MAX = 5000000
L = []*(MAX/2+2)
R = []*(MAX/2+2)
cnt = 0


def merge(A, n, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    for i in range(n1):
        L[i] = A[left + i]
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
    
