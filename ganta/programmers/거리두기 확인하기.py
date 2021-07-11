from collections import deque

def check(r,c, place):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    
    q = deque()
    q.appendleft([r,c,0]) 
    visited = [[0] * 5 for _ in range(5)]
    visited[r][c] = 1
    
    while len(q) != 0:
        search = q.pop()
        if search[2] >= 2: break
        
        for i in range(4):
            nr = search[0] + dr[i]
            nc = search[1] + dc[i]
            if nr < 0 or nr >= 5 or nc < 0 or nc >= 5: continue
            if visited[nr][nc] == 1: continue
            
            if place[nr][nc] == "P": return False
            elif place[nr][nc] == "X": continue
            visited[nr][nc] = 1
            q.appendleft([nr,nc,search[2] + 1])
                
    return True

def search(place):
    for r in range(0,5):
        for c in range(0,5):
            if place[r][c] == 'P':
                if not check(r,c,place):
                    return False
    return True
    
def solution(places):
    answer = []
    
    for place in places:
        if search(place):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer