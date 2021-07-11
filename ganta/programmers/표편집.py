from bisect import bisect_left

board = []
remove_storage = []
remove_stack = []
    
def cancel(location):
    global board
    global remove_storage
    global remove_stack
    
    remove_stack.append(location)
    remove_storage[location] = 1
    
    for i in range(location, len(board)):
        if remove_storage[i] == 0:
            return i
    
    for i in range(location - 1, - 1, -1):
        if remove_storage[i] == 0:
            return i

def re(location):
    global board
    global remove_storage
    global remove_stack
    
    search = remove_stack.pop()
    remove_storage[search] = 0
    
    return location

def up(location, num):
    cnt = 1
    zero_count = 0
    while True:
        if remove_storage[location - cnt] == 0:
            zero_count += 1
        if zero_count == num:
            break    
        cnt += 1

    return location - cnt

def down(location, num):
    cnt = 1
    zero_count = 0
    while True:
        if remove_storage[location + cnt] == 0:
            zero_count += 1
        if zero_count == num:
            break
        cnt += 1
    return location + cnt
    
def solution(n, k, cmd):
    global board
    global remove_storage
    global remove_stack
    
    current_location = k
    answer = ''
    
    for i in range(n):
        board.append(i)
    remove_storage = [0] * n
    
    for command in cmd:
        print(command)
        if command == "C": current_location = cancel(current_location)
        elif command == "Z": current_location = re(current_location)
        else:
            c, num = command.split()
            num = int(num)
            if c == "D": current_location = down(current_location, num)
            elif c == "U": current_location = up(current_location, num)
        print("remove storage", remove_storage)
        print("current location", current_location)
                
    for i in range(n):
        if remove_storage[i] == 0: answer += 'O'
        else: answer += 'X'
                
    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))