n = int(input())
s = [int(_) for _ in input().split()]
q = int(input())
t = [int(_) for _ in input().split()]


def Binary_Search(A, key):
    A_left = 0
    A_right = n
    while A_left < A_right:
        mid = (A_right+A_left) // 2
        if A[mid] < key:
            A_left = mid+1
        elif key < A[mid]:
            A_right = mid
        else:
            return mid
    return "Not_Found"


sol_coun = 0
for i in t:
    if Binary_Search(s, i) != "Not_Found":
        sol_coun += 1
    else:
        continue
print(sol_coun)
