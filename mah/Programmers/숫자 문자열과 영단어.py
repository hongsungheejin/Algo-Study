nums = {
    "zero":'0', "one":'1', "two":'2', "three":'3', "four":'4',
    "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'
}

def solution(s):
    answer = []
    
    sub_str = ""
    for i in range(len(s)):
        if not s[i].isdigit():
            sub_str += s[i]
        else:
            answer.append(str(s[i]))
        
        if sub_str in nums:
            answer.append(nums[sub_str])
            sub_str = ""
    
    return int("".join(answer))