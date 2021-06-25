N = int(input())
brr = []
tem_str = ""

answer = 0


def che_fun():
    che = 1
    for case in brr:
        b = 0
        s = 0
        for i in range(3):
            if tem_str[i] == case[0][i]:
                s += 1
            elif tem_str[i] in case[0]:
                b += 1
        if s != case[1] or b != case[2]:
            che = 0
    return che


def fun(dep):
    global tem_str
    global answer
    if dep == 3:
        answer += che_fun()
        return

    for i in range(1, 10):
        if str(i) in tem_str:
            continue
        tem_str = tem_str + str(i)
        fun(dep+1)
        tem_str = tem_str[:-1]


for i in range(N):
    arr = list(map(int, input().split()))
    arr[0] = str(arr[0])
    brr.append(arr)

fun(0)
print(answer)
