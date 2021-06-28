from itertools import permutations

N = int(input())
candis = {i:candi for i, candi in enumerate(permutations([1,2,3,4,5,6,7,8,9], 3))}
remove_set = set()

for n in range(N):
    num, strike, ball = map(int, input().split())
    num = list(map(int, list(str(num))))
    
    for i in candis:
        if i in remove_set: continue
        strike_cnt, ball_cnt = 0, 0
        
        for t, g in zip(num, candis[i]):
            if t == g: strike_cnt += 1
            elif t in candis[i]: ball_cnt += 1
            
        if strike_cnt != strike or ball_cnt != ball:
            remove_set.add(i)

print(len(candis) - len(remove_set))