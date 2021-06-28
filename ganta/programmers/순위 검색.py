from itertools import combinations
from collections import defaultdict

info_dict = defaultdict(list)

def solution(info, query):
    answer = []
    
    for combi in info:
        combi = combi.split()
        score = combi[-1]
        combi = combi[:-1]
        for i in range(5):
            for pick in combinations(combi,i):
                info_dict["".join(pick)].append(int(score))
    
    for k,v in info_dict.items():
        info_dict[k] = sorted(v)
                
    for q in query:
        q = q.split(" and ")
        l, score = q[-1].split()
        score = int(score)
        k = ""
        for check in q[:-1]:
            if check == '-':
                continue
            k += check
        if l != '-':
            k += l
        search_list = info_dict[k]
        
        if len(search_list) == 0:
            answer.append(0)
        else:
            l, r = 0, len(search_list)

            while l != r and l != len(search_list):
                m = (l + r) // 2

                if search_list[m] >= score:
                    r = m
                else:
                    l = m + 1
            answer.append(len(search_list) - l)
        
    
    return answer