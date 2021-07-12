def solution(prices):
    time = -1
    stack = []
    answer = [0] * len(prices)
    
    prices = prices[::-1]
    while prices:
        time += 1
        if time == 0:
            stack.append([time, prices.pop()])
        else:
            cur = prices[-1]
            if cur >= stack[-1][1]:
                stack.append([time, prices.pop()])
            else:
                while stack and cur < stack[-1][1]:
                    pos, _ = stack.pop()
                    answer[pos] = time - pos
                stack.append([time, prices.pop()])
    
    for pos, _ in stack:
        answer[pos] = time - pos
    
    return answer