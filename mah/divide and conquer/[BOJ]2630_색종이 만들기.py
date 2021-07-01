N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

blue=0
white=0

def divide_concquer(sub_paper, size):
    global white, blue
    
    # 한변의 길이라도 1보다 작으면 리턴
    if size < 1:
        return
    
    count = 0
    for row in sub_paper:
        count += sum(row)
    
    if count == 0:
        white += 1
        return
    elif count == size**2:
        blue += 1
        return
    else:
        half = size//2
        divide_concquer([[sub_paper[y][x] for y in range(half)] for x in range(half)], half) # 좌상단
        divide_concquer([[sub_paper[y][x+half] for y in range(half)] for x in range(half)], half) # 우상단
        divide_concquer([[sub_paper[y+half][x] for y in range(half)] for x in range(half)], half) # 좌하단
        divide_concquer([[sub_paper[y+half][x+half] for y in range(half)] for x in range(half)], half) # 우하단
        
        
divide_concquer(paper, N)
print(white)
print(blue)