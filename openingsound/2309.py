import sys

l = []
answer = [0]*7
find_ans = 0


def fun(idx, dep, tem_ans):
    if dep == 7:
        if tem_ans == 100:
            return 1
        return 0

    for i in range(idx, 9):
        answer[dep] = l[i]
        tem_ans += l[i]
        if fun(i+1, dep+1, tem_ans) == 1:
            return 1
        tem_ans -= l[i]

    return 0


for i in range(9):
    tem = int(input())
    l.append(tem)

fun(0, 0, 0)
answer.sort()
#print("-- 출력 --")
for i in answer:
    print(i)
