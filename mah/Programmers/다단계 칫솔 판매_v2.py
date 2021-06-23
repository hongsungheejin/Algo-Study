from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    
    tree = {}
    money = defaultdict(int)
    
    for s, m in zip(enroll, referral):
        tree[s] = m
    
    new_seller = defaultdict(list)
    for idx, s in enumerate(seller):
        new_seller[s].append(amount[idx] * 100)
    
    for idx, (node, earns) in enumerate(new_seller.items()):
        money[node] += sum(earns)
        
        while node != "-":
            parent = tree[node]
            
            gives = [earn//10 for earn in earns if earn//10 != 0]
            give = sum(gives)
            
            money[node] -= give
            money[parent] += give
            
            node = parent
            earns = gives
    
    for node in enroll:
        if node in money: answer.append(money[node])
        else: answer.append(0)
    return answer