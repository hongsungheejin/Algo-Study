N, L = list(map(int, input().split()))
leaks = sorted(list(map(int, input().split())))

start = leaks[0]
end = start + L - 1

count = 1
for i in leaks[1:]:
    if i <= end: continue
    else:
        count += 1
        start = i
        end = start + L - 1
        
print(count)