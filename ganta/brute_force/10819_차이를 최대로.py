from itertools import permutations

if __name__ == '__main__':
    N = int(input())
    num_list = list(map(int, input().split()))

    ans = -1

    for pick in permutations(num_list,N):
        temp = 0
        for i in range(0, len(pick)- 1):
            temp += abs(pick[i] - pick[i+1])
        ans = max(ans, temp)
    
    print(ans)