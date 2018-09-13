n = int(input())
q_tmp = [input().split() for i in range(n)]
q = []
for i in range(n):
    if len(q_tmp[i]) > 1:
        q.append([q_tmp[i][0], q_tmp[i][1]])
    else:
        q.append(q_tmp[i][0])
ans = []
# print(q)
for i in range(n):
    # print("q[i]", q[i])
    # print("q[i][0]", q[i][0])
    # print(ans)
    if q[i][0] == "insert":
        ans.insert(0, q[i][1])
    elif q[i][0] == "delete":
        for j in range(len(ans)):
            if ans[j] == q[i][1]:
                ans.pop(j)
                break
    elif q[i] == "deleteFirst":
        # print("hoge")
        ans.pop(0)
    elif q[i] == "deleteLast":
        # print("hoge2")
        ans.pop(len(ans)-1)
for i in range(len(ans)-1):
    print(ans[i], end=" ")
print(ans[len(ans)-1])
