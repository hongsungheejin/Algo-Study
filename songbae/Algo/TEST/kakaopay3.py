from collections import Counter
def solution(line1,line2):
  answer=0
  size=len(line2)
  answer+=line1.count(line2)
  temp='_'
  while 1:
    now=temp.join(line2)
    if len(now)>len(line1):break
    for i in range(len(line1)-len(line2)):
      cnt=0
      for j in range(len(line2)):
        if line2[j]=='_':continue
        if line2[j]==line1[i+j]:cnt+=1
      if cnt==size:answer+=1
    temp+='_'
  return answer





print(solution('abbbcbbb','bbb'))