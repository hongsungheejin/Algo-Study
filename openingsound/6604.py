arr = [0] * 14
tem = []


def fun(idx, dep, limit_dep):
    if dep == 6:
        for i in range(dep):
            print(arr[i], end=' ')
        print()
        return 0

    for i in range(idx, limit_dep):
        arr[dep] = tem[i+1]
        if fun(i+1, dep+1, limit_dep) == 1:
            return 1

    return 0


while True:
    tem = list(map(int, input().split()))
    if tem[0] == 0:
        break

    #print("arr : ", arr)
    fun(0, 0, tem[0])
    print()
