a,b,c=map(int,input().split())
cnt=0
temp=a%c
a=1
while (1<<cnt)<=b:
  if (1<<cnt) &b:
    a*=temp%c
    a%=c
  cnt+=1
  temp=temp**2%c
print(a%c)

