from itertools import combinations
temp = set()


def solution(word):
    a = ['A', 'E', 'I', 'O', 'U', 'A', 'E', 'I', 'O', 'U', 'A', 'E',
         'I', 'O', 'U', 'A', 'E', 'I', 'O', 'U', 'A', 'E', 'I', 'O', 'U']
    temp.update(a)
    for i in combinations(a, 2):
        temp.add(''.join(i))
    for i in combinations(a, 3):
        temp.add(''.join(i))
    for i in combinations(a, 4):
        temp.add(''.join(i))
    for i in combinations(a, 5):
        temp.add(''.join(i))
    T = list(temp)
    T = sorted(temp)
    for idx, i in enumerate(T):
        if word == i:
            answer = idx+1
    return answer
