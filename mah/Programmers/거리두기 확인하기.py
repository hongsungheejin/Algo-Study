def solution(places):
    answer = []
    
    for place in places:
        candis = [[x, y] for x in range(5) for y in range(5) if place[x][y] == "P"]

        flag = True
        for i in range(len(candis)):
            for j in range(i+1, len(candis)):
                start, end = candis[i], candis[j]
                
                dist = abs(start[0]-end[0]) + abs(start[1]-end[1])
                if dist > 2: continue
                elif dist == 1: flag = False
                else:
                    min_x, max_x = min(start[0], end[0]), max(start[0], end[0])
                    min_y, max_y = min(start[1], end[1]), max(start[1], end[1])
                    
                    for x in range(min_x, max_x+1):
                        for y in range(min_y, max_y+1):
                            if place[x][y] == "O":
                                flag = False
                                break
                if not flag:
                    break
                    
            if not flag:
                break
        
        if flag: answer.append(1)
        else: answer.append(0)
    
    return answer