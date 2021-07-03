import sys
input = sys.stdin.readline

A, B, C = list(map(int, input().split()))

def solve(A, B):
    if B == 1:
        return A % C
    else:
        prod = solve(A, B//2)
        
        # 짝수/홀수 나눠서
        if B % 2 == 0: return (prod ** 2) % C
        else: return (prod ** 2) * A % C
        
print(solve(A, B))