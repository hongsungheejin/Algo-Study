from itertools import combinations

if __name__ == '__main__':
    height_list = []

    for _ in range(9):
        height_list.append(int(input()))

    idx_list = [i for i in range(9)]

    res_list = []

    for pick in combinations(idx_list, 7):
        temp = 0
        for p in pick:
            temp += height_list[p]
        if temp == 100:
            res_list = pick
            break
    
    res = []
    for r in res_list:
        res.append(height_list[r])
    
    res.sort()

    for n in res:
        print(n)