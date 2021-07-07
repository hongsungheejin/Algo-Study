def solution(S, pattern):
    answer = 0
    now = sorted(pattern)
    now = "".join(now)
    for i in range(len(S)-len(pattern)+1):
        temp = sorted(S[i:i+len(pattern)])
        temp = "".join(temp)
        if temp == now:
            answer += 1
    return answer


