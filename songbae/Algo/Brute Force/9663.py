n = int(input())
col, row = 1 << 15, 1 << 15
upper, down = 1 << 30, 1 << 30
answer = 0


def dfs(idx, cnt, col, row, upper, down):
    global answer
    if cnt == n:
        return 1
    bit_idx=1<<idx
    up=1<<(idx+15)
    do=1<<idx
    for j in range(n):
        bit = 1 << j
        up = 1 >> j
        do = 1 << j
        if col & bit_idx or row & bit or upper & up or down & do:continue
        answer+=dfs(idx+1, cnt+1, col | bit_idx, row | bit, upper | up, down | do)
    return answer
print(dfs(0, 0, col, row, upper, down))

