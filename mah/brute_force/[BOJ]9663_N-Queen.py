import sys
input = sys.stdin.readline

N = int(input())

cols = [0 for _ in range(N)]
l_diags = [0 for _ in range(2*N-1)]
r_diags = [0 for _ in range(2*N-1)]


ans = 0
def dfs(depth):
    global ans
    
    if depth == N:
        ans += 1
    else:
        for col in range(N):
            if cols[col] or l_diags[depth+col] or r_diags[depth-col+N-1]: continue
            
            cols[col] = 1
            l_diags[depth+col] = 1
            r_diags[depth+N-1-col] = 1
            dfs(depth+1)
            cols[col] = 0
            l_diags[depth+col] = 0
            r_diags[depth+N-1-col] = 0

dfs(0)
print(ans)    