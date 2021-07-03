import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

def custom_multiply(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A
    else:
        if B % 2 == 0:
            result = custom_multiply(A, B // 2, C)
            return pow(result, 2) % C
        else:
            result = custom_multiply(A, B - 1, C)
            return result * A

print(custom_multiply(A, B, C) % C)