N, M = map(int, input().split())

chess_board = []

for i in range(N):
  chess_board.append(input())

repair = []

for i in range(N - 7):
  for j in range(M - 7):
    case_W = 0
    case_B = 0
    for k in range(i, i + 8):
      for w in range(j, j + 8):
        if (k + w) % 2 == 0:
          if chess_board[k][w] != 'W':
            case_W += 1
          if chess_board[k][w] != 'B':
            case_B += 1
        else:
          if chess_board[k][w] != 'B':
            case_W += 1
          if chess_board[k][w] != 'W':
            case_B += 1
    repair.append(case_W)
    repair.append(case_B)

# print(repair)
print(min(repair))