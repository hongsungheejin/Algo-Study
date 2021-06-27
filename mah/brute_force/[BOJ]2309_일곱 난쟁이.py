hs = [int(input()) for _ in range(9)]

def search(sub_h, idx):
    if sum(sub_h) == 100 and len(sub_h) == 7:
        for h in sorted(sub_h):
            print(h)
        exit()
    elif idx >= 9 or len(sub_h) == 7: return 0
    
    for i in range(idx, 9):
        sub_h.append(hs[i])
        search(sub_h, i+1)
        sub_h.pop()

search([], 0)