from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    
    tree = {}
    money = defaultdict(int)
    
    for s, m in zip(enroll, referral):
        tree[s] = m
    
    for idx, node in enumerate(seller):
        earn = amount[idx] * 100
        money[node] += earn
        
        while node != "-":
            parent = tree[node]
            
            give = earn // 10
            if give < 1: break
                
            money[node] -= give
            money[parent] += give
            
            node = parent
            earn = give
            
    
    for node in enroll:
        if node in money: answer.append(money[node])
        else: answer.append(0)


    return answer