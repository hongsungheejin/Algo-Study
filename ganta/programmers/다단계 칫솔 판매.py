parent = []
amount_list = []
personal_id = {}

def distribute(search, amount):
    if parent[search] == search or int(amount * 0.1) < 1:
        amount_list[search] += amount
        return
    
    amount_list[search] += (amount -  int(amount * 0.1))
    distribute(parent[search], int(amount * 0.1))

def solution(enroll, referral, seller, amount):
    answer = []
       
    personal_id["-"] = 0
    parent.append(0)
    amount_list.append(0)
    
    for i, e in enumerate(enroll):
        personal_id[e] = i+1
        parent.append(0)
        amount_list.append(0)
    
    for e, r in zip(enroll, referral): parent[personal_id[e]] = personal_id[r]   
    for s, a in zip(seller, amount): distribute(personal_id[s], a * 100)
    
    return amount_list[1:]