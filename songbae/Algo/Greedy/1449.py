n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] *= 2
m *= 2
temp = [0]*4000
for i in arr:
    if not temp[i]:
        temp[i] += 1
answer = 0
for i in range(2002):
    if temp[i] == 1:
        answer += 1
        for j in range(m+1):
            temp[i+(j-1)] -= 1
print(answer)
