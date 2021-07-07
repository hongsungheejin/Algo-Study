import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

left_nodes = [0] * (n+1)
for i in range(n):
    left_nodes[inorder[i]] = i


if n==1:
    print(*inorder)
elif n==2:
    print(*postorder[::-1])
else:
    def traversal(in_s, in_e, po_s, po_e):
        if in_s > in_e or po_s > po_e:
            return

        p = postorder[po_e]
        print(p, end=" ")
        
        left = left_nodes[p] - in_s
        right = in_e - left_nodes[p]
        
        traversal(in_s, in_s+left-1, po_s, po_s+left-1)
        traversal(in_e-right+1, in_e, po_e-right, po_e-1)

    traversal(0, n-1, 0, n-1)