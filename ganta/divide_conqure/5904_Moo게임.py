N = 0

def divide_conqure(check_moo, check_index):
    global N
    global moo_dict
    
    if check_moo == 0:
        if check_index == 0:
            print("m")
            exit()
        if check_index==1 or check_index==2:
            print("o")
            exit()

    range1 = moo_dict[check_moo-1]
    range2 = moo_dict[check_moo-1] + moo_dict[check_moo] - (moo_dict[check_moo-1]*2)
    
    if check_index <= range1 - 1:
        divide_conqure(check_moo-1, check_index)
    elif check_index > range1 - 1 and check_index <= range2 -1:
        if check_index - range1 == 0: print("m")
        else: print("o")
        exit()
    else:
        divide_conqure(check_moo-1, check_index - range2)
        
if __name__ == '__main__':
    N = int(input()) - 1 
    check = 3
    temp_check = 3 
    cnt = 0
    moo_dict = {}
    while True:
        moo_dict[cnt] = check
        if check-1 >= N:
            moo_dict[cnt] = check
            break
        cnt += 1
        check = (check * 2) + 1  + (cnt + 2)
        
    divide_conqure(cnt,N)
        