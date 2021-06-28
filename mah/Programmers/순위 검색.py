from itertools import combinations

def solution(info, query):
    answer = []
    
    
    db = {}
    for candi in info:
        lang, borf, jors, corp, score = candi.split()
        score = int(score)
        indexs = [0, 1, 2, 3]
        
        for c in range(5):
            i_comb = combinations(indexs, c)
            for comb in i_comb:
                querys = [lang, borf, jors, corp]
                for i in comb:
                    querys[i] = "-"
                
                querys = "".join(querys)
                if querys in db: 
                    db[querys].append(score)
                else:
                    db[querys] = []
                    db[querys].append(score)
    
    for v in db.values():
        v.sort()
    
    for q in query:
        q = q.split(" and ")
        corp, score = q[-1].split()
        q[-1] = corp
        score = int(score)
        
        q = "".join(q)
        if q in db: 
            score_list = db[q]
            score_len = len(score_list)
            l, r = 0, score_len
            
            while l!=r and l!=score_len:
                m = (l + r) // 2
                
                if score_list[m] >= score:
                    r = (l+r) // 2
                else:
                    l = (l+r) // 2 + 1
            
            answer.append(score_len-l)
        else: answer.append(0)
        
    return answer