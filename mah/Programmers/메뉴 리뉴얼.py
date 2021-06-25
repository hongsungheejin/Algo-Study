from itertools import combinations

def solution(orders, course):
    candi = {}
    course = set(course)
    for order in orders:
        order = sorted(order)
        
        for i in range(2, len(order)+1):
            for combi in combinations(order, i):
                combi = "".join(combi)
                if combi in candi:
                    candi[combi] += 1
                else:
                    candi[combi] = 1
    
    answer = []
    candis = {k:v for k, v in sorted(candi.items(), key=lambda x: (len(x[0]), x[1])) if v>=2}
    for c in course:
        tmp = {}
        max_v = 0
        for k, v in sorted(candis.items(), key=lambda x:x[0]):
            if len(k) == c:
                max_v = max(max_v, v)
                if v in tmp: tmp[v].append(k)
                else: tmp[v] = [k]
        
        if max_v in tmp:
            answer.extend(tmp[max_v])
    
    return sorted(answer)