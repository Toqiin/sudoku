def print_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-------------------------------")
        for j in range(9):
            if j == 8:
                print(bo[i][j])
            else:
                if j % 3 == 0 and j != 0:
                    print("|  ", end="")

                print(str(bo[i][j]) + "  ", end="")
    print("")


def find_first_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return i, j
    return None


def valid(bo, num, pos):
    for j in range(9):
        if bo[pos[0]][j] == num:
            return False

    for i in range(9):
        if bo[i][pos[1]] == num:
            return False

    box_x = pos[0] // 3
    box_y = pos[1] // 3

    start_x = box_x * 3
    end_x = start_x + 3

    start_y = box_y * 3
    end_y = start_y + 3

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if bo[i][j] == num:
                return False

    return True


def solve(bo):
    found = find_first_empty(bo)
    if not found:
        return True
    else:
        x = found[0]
        y = found[1]

    for i in range(1, 10):
        if valid(bo, i, found):
            bo[x][y] = i

            if solve(bo):
                return True
            else:
                bo[x][y] = 0

    return False


def gen_solved(bo):
    new_bo = list(bo)
    solve(new_bo)
    return new_bo

board = [[1, 0, 8, 0, 0, 0, 0, 0, 3],
         [0, 0, 9, 8, 1, 0, 6, 0, 0],
         [0, 0, 6, 5, 2, 0, 0, 0, 0],
         [4, 7, 1, 9, 0, 2, 3, 0, 0],
         [0, 0, 3, 0, 4, 5, 0, 0, 0],
         [0, 0, 0, 0, 8, 1, 0, 6, 0],
         [3, 9, 7, 0, 0, 8, 0, 2, 4],
         [8, 6, 2, 1, 0, 0, 0, 0, 9],
         [0, 0, 0, 0, 3, 0, 7, 0, 6]]


