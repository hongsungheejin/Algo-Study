import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    
    class_list = []
    ans = 0
    end_time = 0
    for _ in range(N):
        class_list.append(list(map(int, input().split())))
        
    class_list.sort(key = lambda x : (x[1], x[0]))
    
    for c in class_list:
        if end_time <= c[0]:
            ans += 1
            end_time = c[1]

    print(ans)