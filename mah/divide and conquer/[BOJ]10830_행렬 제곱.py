import sys
sys.setrecursionlimit(10*6)

N, B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
I = [[1 if i==j else 0 for i in range(N) ] for j in range(N)]

def sub(a_row, b_row):
    return sum([a*b for a, b in zip(a_row, b_row)])

def mul(a, b):
    return [[sub(a_row, b_row)%1000 for b_row in list(zip(*b))] for a_row in a]
    
def solve(A, B):
    if B == 1:
        return mul(A, I)
    else:
        nB = B//2
        
        if B % 2 != 0:
            return mul(solve(mul(A, A), nB), A)
        else:
            return solve(mul(A, A), nB)
        
ans = solve(A, B)
for row in ans:
    print(*row)