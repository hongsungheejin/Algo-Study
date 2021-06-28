if __name__ == '__main__':
    line = []
    
    for _ in range(11):
        a, b = map(int,input().split())
        line.append([a,b])
        
    line.sort()
    
    t = 0
    ans = 0
    for l in line:
        t += l[0]
        ans += t + 20 * l[1]
    print(ans)