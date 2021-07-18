n=int(input())
s=[0]*1000
s[0]=3
cnt=1
while 1:
  s[cnt]=s[cnt-1]+cnt+3+s[cnt-1]
  if s[cnt]>n:
    break
  cnt+=1
answer=['-1','m','o','o']
def recur(now,cnt):
  if cnt==0:
    return answer[now]
  if now<=s[cnt-1]:
    return recur(now,cnt-1)  
  elif now>s[cnt-1]+cnt+3:
    return recur(now-s[cnt-1]-cnt-3,cnt-1)
  else:
    if now==s[cnt-1]+1:
      return 'm'
    return 'o'
print(recur(n,cnt))


