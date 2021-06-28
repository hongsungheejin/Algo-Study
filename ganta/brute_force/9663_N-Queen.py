ans = 0
N = 0
column_check = []
diagonal_check1 = []
diagonal_check2 = []

def dfs(n):
    global N
    global ans
    global cloumn_check
    global diagonal_check1
    global diagonal_check2
    
    # row n, column i
    if n == N:
        ans += 1
        return
    else:
        for i in range(N):            
            if column_check[i] == 0 and diagonal_check1[n + i] == 0 and diagonal_check2[n-i+N-1] == 0:
                column_check[i] = 1
                diagonal_check1[n + i] = 1
                diagonal_check2[n-i+N-1] = 1
                dfs(n+1)
                column_check[i] = 0
                diagonal_check1[n + i] = 0
                diagonal_check2[n-i+N-1] = 0

if __name__ == '__main__':
    N = int(input())
    column_check = [0] * N # 열
    diagonal_check1 = [0] * (2*N-1)
    diagonal_check2 = [0] * (2*N-1)
    
    dfs(0)
    
    print(ans)
    