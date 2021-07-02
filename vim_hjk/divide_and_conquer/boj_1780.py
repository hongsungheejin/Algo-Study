import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

zero = 0
one = 0
minus_one = 0

def cut(x, y, N):
    global zero
    global one
    global minus_one
    
    check = paper[x][y]
    one_third = N // 3

    for i in range(x, x + N):
        for j in range(y, y + N):
            if check != paper[i][j]:
                cut(x, y, one_third)
                cut(x, y + one_third, one_third)
                cut(x, y + 2 * one_third, one_third)
                cut(x + one_third, y, one_third)
                cut(x + one_third, y + one_third, one_third)
                cut(x + one_third, y + 2 * one_third, one_third)
                cut(x + 2 * one_third, y, one_third)
                cut(x + 2 * one_third, y + one_third, one_third)
                cut(x + 2 * one_third, y + 2 * one_third, one_third)
                return
    
    if check == 0:
        zero += 1
        return

    if check == 1:
        one += 1
        return

    if check == -1:
        minus_one += 1
        return

cut(0, 0, N)
print(minus_one)
print(zero)
print(one)