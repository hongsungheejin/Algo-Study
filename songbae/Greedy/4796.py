cnt=1
while 1:
  p,l,v= map(int,input().split())
  if p==0 and v==0 and l==0 : break
  T=v//l
  res=v%l
  print(f'Case {cnt}: {T*p+min(res,p)}')
  cnt+=1

