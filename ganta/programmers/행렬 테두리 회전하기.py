board = []


def rotate_func(query):
    x1, y1, x2, y2 = query
    
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    
    check_list = []
    
    temp_num1 = board[x1][y1]
    check_list.append(temp_num1)
    
    # 상
    for i in range(y1,y2):
        temp_num2 = board[x1][i+1]
        board[x1][i+1] = temp_num1
        temp_num1 = temp_num2
        check_list.append(temp_num1)
         
    # 우
    for i in range(x1, x2):
        temp_num2 = board[i+1][y2]
        board[i+1][y2] = temp_num1
        temp_num1 = temp_num2
        check_list.append(temp_num1)
        
    # 하
    for i in range(y2,y1, -1):
        temp_num2 = board[x2][i-1]
        board[x2][i-1] = temp_num1
        temp_num1 = temp_num2
        check_list.append(temp_num1)
    
    # 좌
    for i in range(x2, x1, -1):
        temp_num2 = board[i-1][y1]
        board[i-1][y1] = temp_num1
        temp_num1 = temp_num2
        check_list.append(temp_num1)
    
    return min(check_list)


def solution(rows, columns, queries):
    answer = []
    insert_num = 1
    
    for _ in range(rows):
        temp = []
        for _ in range(columns):
            temp.append(insert_num)
            insert_num += 1
        board.append(temp)
    
    for q in queries:
        answer.append(rotate_func(q))
    
    return answer