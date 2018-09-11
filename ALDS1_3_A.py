# スタックの実装
# 後入れ先出し
a = input().split()
stack_list = []
index = -1
operand = ["+", "-", "*"]
for i in range(len(a)):
    if a[i] not in operand:
        stack_list.append(int(a[i]))
        index += 1
    else:
        if a[i] == "+":
            operated2 = stack_list.pop(index)
            index -= 1
            operated1 = stack_list.pop(index)
            index -= 1
            stack_list.append(operated1 + operated2)
            index += 1
        elif a[i] == "-":
            operated2 = stack_list.pop(index)
            index -= 1
            operated1 = stack_list.pop(index)
            index -= 1
            stack_list.append(operated1 - operated2)
            index += 1
        elif a[i] == "*":
            operated2 = stack_list.pop(index)
            index -= 1
            operated1 = stack_list.pop(index)
            index -= 1
            stack_list.append(operated1 * operated2)
            index += 1
print(stack_list[index])
