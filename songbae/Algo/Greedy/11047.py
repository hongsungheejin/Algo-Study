n,k = map(int, input().split())
arr= [int(input()) for i in range(n)]
cnt=0
for i in arr[::-1]:
  cnt+=k//i
  k=k%i
print(cnt)