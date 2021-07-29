import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, H = map(int,input().split())
    obstacles = [int(input()) for _ in range(N)]
    even_obstacles = []
    odd_obstacles = []
    h_check = [0] * (H+1)
    temp_h_check = [0] * (H+1)
    
    for i, v in enumerate(obstacles):
        if i % 2 == 0:
            even_obstacles.append(v)
        else:
            odd_obstacles.append(v)
    
    for v in even_obstacles:
        h_check[v] += 1
    for v in odd_obstacles:
        temp_h_check[H - (v-1)] += 1
    
    even_temp = 0
    odd_temp = 0
    for i in range(0, len(h_check)):
        if h_check[len(h_check) -1 -i] == 0:
            h_check[len(h_check) -1 -i] = even_temp
        else:
            even_temp += h_check[len(h_check) -1 -i]
            h_check[len(h_check) -1 -i] = even_temp
        
        if temp_h_check[i] == 0:
            temp_h_check[i] = odd_temp
        else:
            odd_temp += temp_h_check[i]
            temp_h_check[i] = odd_temp
    
    for i in range(0, len(h_check)):
        h_check[i] += temp_h_check[i]
    h_check[0] = 987654321
    min_v = min(h_check)
    print(min_v, h_check.count(min_v))
    