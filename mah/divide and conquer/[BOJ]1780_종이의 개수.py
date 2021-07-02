import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


minus = 0
ones = 0
zeros = 0


def divide_conquer(x, y, size):
    global minus, zeros, ones
    
    if size < 1: return 0
    else:
        token = paper[x][y]
        for i in range(x, x+size):
            for j in range(y, y+size):
                if token != paper[i][j]: 
                    token = -2
                    break
            
            if token == -2: break
                
        
        if token == 0:
            zeros += 1
            return
        elif token == -1:
            minus += 1
            return
        elif token == 1:
            ones += 1
            return
        else:
            next_size = size // 3
            
            divide_conquer(x, y, next_size)
            divide_conquer(x, y+next_size, next_size)
            divide_conquer(x, y+next_size*2, next_size)
            
            divide_conquer(x+next_size, y, next_size)
            divide_conquer(x+next_size, y+next_size, next_size)
            divide_conquer(x+next_size, y+next_size*2, next_size)
            
            
            divide_conquer(x+next_size*2, y, next_size)
            divide_conquer(x+next_size*2, y+next_size, next_size)
            divide_conquer(x+next_size*2, y+next_size*2, next_size)
            

divide_conquer(0, 0, N)
print(minus)
print(zeros)
print(ones)