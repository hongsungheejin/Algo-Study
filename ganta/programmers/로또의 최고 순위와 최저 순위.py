def solution(lottos, win_nums):
    ans_dict = {
        0 : 6,
        1 : 6,
        2 : 5,
        3 : 4,
        4 : 3,
        5 : 2,
        6 : 1
    }
    
    ans_list = [0,0]
        
    for lotto in lottos:
        if lotto == 0:
            ans_list[0] += 1
            continue
        if win_nums.count(lotto) != 0:
            ans_list[0] += 1
            ans_list[1] += 1
    
    return [ans_dict[ans_list[0]], ans_dict[ans_list[1]]]