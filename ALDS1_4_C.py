def str_to_nume(word):
    ans = ""
    for _ in word:
        if _ == "A":
            ans += ("1")
        elif _ == "C":
            ans += ("2")
        elif _ == "G":
            ans += ("3")
        elif _ == "T":
            ans += ("4")
    return ans


def convert_type(word):
    return int(str_to_nume(word))

sols = []
n = int(input())
m = 111111111111
h = [0 for i in range(m)]
# print("hoge")
for i in range(n):
    col = input().split()
    if col[0] == "insert":
        h[convert_type(col[1])] = 1
    else:
        if h[convert_type(col[1])] == 1:
            print("yes")
        else:
            print("no")
