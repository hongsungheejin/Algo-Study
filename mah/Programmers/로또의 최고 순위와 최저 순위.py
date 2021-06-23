def solution(lottos, win_nums):
    win_nums = set(win_nums)
    
    eq = 0
    zeros = 0
    for lotto in lottos:
        if lotto == 0: zeros += 1
        elif lotto in win_nums:
            win_nums.remove(lotto)
            eq += 1
    
    mapping = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    return [mapping[eq+zeros], mapping[eq]]