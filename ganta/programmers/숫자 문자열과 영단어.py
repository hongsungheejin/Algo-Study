def solution(s):
    answer = ""
    word_dict = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" :  "5",
        "six" :  "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }
    idx = 0
    
    while True:
        if idx >= len(s):
            break
        
        if s[idx].isdigit():
            answer += s[idx]
            idx += 1
            continue
        
        for k, v in word_dict.items():
            if s[idx: idx + len(k)] == k:
                answer += v
                idx += len(k)
                continue
    
    return int(answer)