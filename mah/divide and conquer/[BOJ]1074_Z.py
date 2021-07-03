N, r, c = list(map(int, input().split()))
size = 2**N

ans = 0
def solve(x, y, size):
    global ans
    
    if x == r and y == c:
        print(ans)
        exit()

    if size == 1:
        ans += 1
        return
    
    if not ((x <= r < x+size) and (y <= c < y+size)):
        ans += size * size
        return
    
    n_size = size // 2
    solve(x, y, n_size)
    solve(x, y+n_size, n_size)
    solve(x+n_size, y, n_size)
    solve(x+n_size, y+n_size, n_size)
            
solve(0,0, 2**N)