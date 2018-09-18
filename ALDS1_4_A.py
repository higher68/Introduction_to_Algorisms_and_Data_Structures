n = int(input())
s = [int(_) for _ in input().split()]
q = int(input())
t = [int(_) for _ in input().split()]


def LinearSearch(key):
    '''
    keyにたどり着いたらbreak
    '''
    tmp_list = s + [key]
    i = 0
    while tmp_list[i] != key:
        i += 1
    if i != n:
        return True
    return False


sum = 0
for key in t:
    judge = LinearSearch(key)
    if judge:
        sum += 1

print(sum)
