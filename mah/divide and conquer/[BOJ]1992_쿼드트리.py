N = int(input())
img = [list(map(int, list(input()))) for _ in range(N)]


def quad_tree(x, y, size):
    if size < 1: return ''
    else:
        cnt = 0
        for i in range(x, x+size):
            cnt += sum(img[i][y:y+size])
            
        if cnt == 0:
            return '0'
        elif cnt == size * size:
            return '1'
        else:
            next_size = size//2
            return "(" + quad_tree(x, y, next_size) + quad_tree(x, y+next_size, next_size) \
                       + quad_tree(x+next_size, y, next_size) + quad_tree(x+next_size, y+next_size, next_size) + ")"
                       
print(quad_tree(0, 0, N))