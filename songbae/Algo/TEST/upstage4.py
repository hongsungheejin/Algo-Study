from collections import deque
def count_internal_nodes(tree):
    T = [[] for i in range(len(tree)+1)]
    root = -1
    cnt=0
    for idx, i in enumerate(tree):
        if i == -1:
           root = idx
        else:
            if not T[i]: cnt+=1
            T[i].append(idx)
    return cnt


tree = [1, 3, 1, -1, 3]
print(count_internal_nodes(tree))  # should print 2
