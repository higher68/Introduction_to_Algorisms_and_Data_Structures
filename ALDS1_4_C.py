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


n = int(input())
m = 1234567890
h = [0 for i in range(m)]
sol_list = []
sol_count = 0
for i in range(n):
    col = input()
    if col[0] == "insert":
        h[convert_type(col[1])] == 1
    else:
        if h[convert_type(col[1])] == 1:
            print("Yes")
        else:
            print("No")
