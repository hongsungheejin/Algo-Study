def print_lotto(nums):
    def inner(sub, idx):
        if len(sub)==6:
            print(*sub)
            return

        s = idx + 1 if sub else 0
        for i in range(s, len(nums)):
            sub.append(nums[i])
            inner(sub, i)
            sub.pop()

    inner([], -1)
    print()

while True:
    k, *nums = list(map(int, input().split()))
    if k == 0: break
    else:
        print_lotto(nums)