def print_lotto(nums):
    def inner(chosen, idx):
        if len(chosen)==6:
            print(*chosen)
            return

        s = idx + 1 if chosen else 0
        for i in range(s, len(nums)):
            chosen.append(nums[i])
            inner(chosen, i)
            chosen.pop()

    inner([], -1)
    print()

while True:
    k, *nums = list(map(int, input().split()))
    if k == 0: break
    else:
        print_lotto(nums)