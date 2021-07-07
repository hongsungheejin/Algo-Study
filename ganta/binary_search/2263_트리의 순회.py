import sys
sys.setrecursionlimit(10**6) 

res = []

n = int(input())
in_order = []
post_order = []
in_order_index  = {}

# 중위랑 후위 인덱스 다르게
def search(in_start, in_end, post_start, post_end):
    
    if in_start > in_end or post_start > post_end:
        return
    
    insert_num = post_order[post_end]
    res.append(insert_num)
    
    left_count = in_order_index[insert_num] - in_start
    right_count = in_end - in_order_index[insert_num]
    
    search(in_start, in_start + left_count - 1, post_start, post_start + left_count - 1) # 왼쪽 고려
    search(in_end - right_count + 1, in_end, post_end - right_count, post_end - 1) # 오른쪽 고려

if __name__ == '__main__':
    
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    
    for i,v in enumerate(in_order):
        in_order_index[v] = i
    
    
    search(0,n-1,0,n-1)
    
    res = list(map(str, res))
    print(" ".join(res))
    