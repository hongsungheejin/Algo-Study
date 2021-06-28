N, M = map(int, input().split())

brr = []
for _ in range(N):
    tem = input()
    brr.append(tem)
answer = 64
for ti in range(N-7):
    for tj in range(M-7):
        tem_ans = [0, 0]
        for i in range(ti, ti+8):
            for j in range(tj, tj+8):

                if (i+j) % 2 == 1:
                    if brr[i][j] == 'W':
                        tem_ans[0] += 1
                    else:
                        tem_ans[1] += 1
                else:
                    if brr[i][j] == 'B':
                        tem_ans[0] += 1
                    else:
                        tem_ans[1] += 1
        answer = min(tem_ans[0], answer, tem_ans[1])

print(answer)
