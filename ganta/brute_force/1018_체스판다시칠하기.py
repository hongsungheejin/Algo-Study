board = []

def change_check(r,c):
    
    cnt1 = 0
    cnt2 = 0

    chr_list = ["W","B"]

    for i in range(r,r + 8):
        idx = (i+1) % 2
        for j in range(c, c + 8):
            if board[i][j] != chr_list[idx]: cnt1 += 1
            idx = (idx + 1) % 2
    
    for i in range(r, r + 8):
        idx = i % 2
        for j in range(c,c + 8):
            if board[i][j] != chr_list[idx]: cnt2 += 1
            idx = (idx + 1) % 2
    
    return min(cnt1, cnt2)


if __name__ == '__main__':
    N, M = map(int, input().split())

    board = [[] for _ in range(N)]
    for i in range(N):
        insert = list(input())
        for c in insert:
            board[i].append(c)

    chr_list = ["W","B"]
    
    ans = 987654321

    for r in range(N - 8 + 1):
        for c in range(M - 8 + 1):
            ans = min(ans, change_check(r,c))

    print(ans)