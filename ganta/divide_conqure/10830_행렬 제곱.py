mat = []
N = 0
B = 0

def print_mat(m):
    for r in m:
        r = map(str, r)
        print(" ".join(r))
    
def multi(a,b):
    res  = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            insert_num = 0
            for k in range(N):
                insert_num += a[i][k] * b[k][j]
            res[i][j] = insert_num % 1000
    return res

def func(m):
    return multi(m,m)

def solve(m,check):
    if check == 2:
        return func(m)
    if check == 1:
        return m
    
    
    if check % 2 == 1:
        return multi(func(solve(m,check//2)), m)
    else:
        return func(solve(m, check//2))
    
if __name__ == '__main__':
    global matrix
    
    N, B = map(int, input().split())
    
    for _ in range(N):
        mat.append(list(map(int, input().split())))
        
    if B == 1:
        identity = [[0] * N for _ in range(N)]
        for i in range(N):
            identity[i][i] = 1
        print_mat(multi(mat,identity))
    else:
        print_mat(solve(mat,B))
