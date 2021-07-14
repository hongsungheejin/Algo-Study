from itertools import combinations

def calc(check_list):
    res = 1 
    for c in check_list:
        res *= c
    return res

if __name__ == '__main__':
    N = int(input())
    num_arr = list(map(int, input().split()))
    
    pick_index = [i for i in range(1, N)]
    
    res = -1
    
    for pick in combinations(pick_index,3):
        temp = calc(num_arr[:pick[0]]) + \
            calc(num_arr[pick[0]: pick[1]]) + \
                calc(num_arr[pick[1]: pick[2]]) + \
                    calc(num_arr[pick[2]: ])
        res = max(res,temp)
    print(res)
    