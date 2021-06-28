
def find_max_sum(numbers):
    prev = -1
    answer, answer1 = 0, 0
    for i in numbers:
        now = i
        if now >= prev:
            answer = max(prev+now, answer)
            prev = now
    prev = -1
    for i in numbers[::-1]:
        now = i
        if now >= prev:
            answer1 = max(prev+now, answer)
            prev = now

    return answer1


if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 11]))
