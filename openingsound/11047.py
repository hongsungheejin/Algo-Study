n, k = map(int, input().split())

ans = 0

for i in range(n):
    tem = int(input())
    ans += k // tem
    k %= tem

print(ans)
