import sys

input = sys.stdin.readline

sdoku = [list(map(int, input().split())) for _ in range(9)]
coordinates = [(x, y) for x in range(9) for y in range(9) if sdoku[x][y] == 0]

base = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

mini = [(0, 3), (3, 6), (6, 9)]

def guess_the_right_answer(index):
    if index == len(coordinates):
        for row in sdoku:
            print(*row)
        sys.exit()

    else:
        x, y = coordinates[index]

        col = [row[y] for row in sdoku]

        row_range = mini[x // 3]
        col_range = mini[y // 3]
        square = [sdoku[i][j] for i in range(row_range[0], row_range[1]) for j in range(col_range[0], col_range[1])]

        for t in base:
            if t not in sdoku[x] and t not in col and t not in square:
                sdoku[x][y] = t
                guess_the_right_answer(index + 1)
                sdoku[x][y] = 0

guess_the_right_answer(0)