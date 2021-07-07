def solution(letters, k):
    answer = ''
    index = [[] for i in range(26)]
    cur = k
    now_idx = -1
    for idx, i in enumerate(letters):
        index[ord(i)-97].append(idx)
    for idx, T in enumerate(index[::-1]):
        for j in T:
            if j < len(letters)-cur and j > now_idx:
                answer += chr(25-idx+97)
                now_idx = j
                cur -= 1
            elif j == len(letters)-cur and j > now_idx:
                res = letters[j:]
                res = ''.join(res)
                answer += res
                return answer
            if cur == 1:
                answer += max(letters[now_idx+1:])
                cur -= 1
            if cur == 0:
                return answer
    return answer


print(solution('zbcdeedfdrpkzz', 4))
