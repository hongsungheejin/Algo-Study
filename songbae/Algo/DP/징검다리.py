from collections import defaultdict


def solution(distance, rocks, n):
  answer=0
  start,end=0,distance
  rocks.sort()
  while start<=end:
    mid=(start+end)//2
    del_s=0
    prev=0
    for rock in rocks:
      if rock-prev<mid:
        del_s+=1
        if del_s>n:break
      else:prev=rock
    if del_s>n:end=mid-1
    else:
       answer=mid
       start=mid+1
  return answer
