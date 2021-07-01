import sys

input = sys.stdin.readline

N = int(input())
confetti = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def cut(N, confetti):
    global white
    global blue

    value_sum = 0
    
    for row in confetti:
        value_sum += sum(row)

    if value_sum == 0:
        white += 1
        return
    elif value_sum == pow(N, 2):
        blue += 1
        return
    else:
        half = N // 2

        quadrant_1 = [[confetti[i][j] for i in range(0, half)] for j in range(0, half)]        
        quadrant_2 = [[confetti[i][j] for i in range(half, N)] for j in range(0, half)]
        quadrant_3 = [[confetti[i][j] for i in range(0, half)] for j in range(half, N)]
        quadrant_4 = [[confetti[i][j] for i in range(half, N)] for j in range(half, N)]

        cut(half, quadrant_1)
        cut(half, quadrant_2)
        cut(half, quadrant_3)
        cut(half, quadrant_4)

cut(N, confetti)
print(white)
print(blue)