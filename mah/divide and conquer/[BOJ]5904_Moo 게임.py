N = int(input())

length = 3
add = 4

while N > length:
    length = length * 2 + add
    add += 1

middle = add - 1
while True:
    prev_len = (length - middle)//2
    
    # 중간부분
    if prev_len < N <= prev_len + middle:
        N -= prev_len
        break
    # 왼쪽
    elif N <= prev_len:
        middle -= 1
        length = prev_len
    # 오른쪽
    elif prev_len + middle < N:
        N -= (prev_len + middle)
        middle -= 1
        length = prev_len


if N==1: print("m")
else: print("o")