import heapq
class ProblemPy:
    @staticmethod
    def solve(n, e, companies, subway_map):
        # IMPLEMENT HERE
        arr=[[] for i in range(n+1)]
        for idx,sub in enumerate(subway_map):
          for j in sub:
            if j==0: continue
            for k,temp in enumerate(subway_map):
              if temp[idx]:
                arr[idx].append((k,temp[idx],0 if companies[idx]==companies[k] else 1))
        start=0
        MAX=1000000000
        dist= [ [MAX,MAX] for i in range(n+1)]
        dist[start][0]=0
        dist[start][1]=0
        queue=list()
        heapq.heappush(queue,(dist[start][0],start,0))
        while queue:
          cur_dist, node,cnt=heapq.heappop(queue)
          if dist[node][0]<cur_dist:continue
          for n_node,value,flag in arr[node]:
            n_cost=value+cur_dist
            n_flag=cnt+1 if flag else cnt
            if n_cost<dist[n_node][0] and n_flag<=dist[n_node][1]:
              dist[n_node][0]=n_cost
              dist[n_node][1]=n_flag
              heapq.heappush(queue,(n_cost,n_node,n_flag))
        

        transfer = dist[e][1]
        cost = dist[e][0]
        return transfer, cost


# DO NOT MODIFY FROM HERE
n = 6
e = 3
companies = [0, 1, 1, 0, 1, 0]
subway_map = [[0, 3, 1, 0, 10, 0], [3, 0, 0, 15, 0, 0], [1, 0, 0, 0, 0, 1], [
    0, 15, 0, 0, 10, 0], [10, 0, 0, 10, 0, 1], [0, 0, 1, 0, 1, 0]]
print(ProblemPy.solve(n, e, companies, subway_map))
