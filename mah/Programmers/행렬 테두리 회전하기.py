from collections import deque

moves = [
    [0, 1],  # 우
    [1, 0],  # 하
    [0, -1], # 좌
    [-1, 0]  # 상
]

def solution(rows, columns, queries):
    answer = []
    
    matrix = [[i+j*columns for i in range(1, columns+1)] for j in range(rows)]
    for y1,x1,y2,x2 in queries:
        y1,x1,y2,x2 = y1-1,x1-1,y2-1,x2-1
        
        check = []
        que = [[y1, x1, matrix[y1][x1]]]
        que = deque(que)
        
        dir = 0
        while que:
            y, x, prev = que.popleft()
            check.append(prev)

            move = moves[dir]
            ny, nx = y + move[0], x + move[1]
            if (ny==y1 and nx==x2) or (ny==y2 and nx==x2) or (ny==y1 and nx==x1) or (ny==y2 and nx==x1):
                dir = (dir+1)%4
            
            if ny == y1 and nx == x1:
                matrix[ny][nx] = prev
                break
            
            que.append([ny, nx, matrix[ny][nx]])
            matrix[ny][nx] = prev
        
        answer.append(min(check))    
    return answer