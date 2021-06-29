N = int(input())

count = 0
board = [0] * N

def dfs(x):
  global count

  if x == N:
    count += 1
    return
  for i in range(N):
    board[x] = i
    if check_promising(x):
      dfs(x + 1)

def check_promising(x):
  for i in range(x):
    if board[x] == board[i] or abs(board[x] - board[i]) == x - i:
      return False
  return True

dfs(0)
print(count)