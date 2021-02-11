import random

import copy

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

board2 = [[9, 9, 9, 9, 9, 9, 9, 9, 9],
          [9, 9, 9, 9, 9, 9, 9, 9, 9],
          [9, 9, 9, 9, 9, 9, 9, 9, 9],
          [9, 9, 9, 9, 9, 9, 9, 9, 9],
          [9, 9, 9, 9, 9, 9, 9, 9, 9],
          [9, 9, 9, 9, 9, 9, 9, 9, 9],
          [9, 9, 9, 9, 9, 9, 9, 9, 9],
          [9, 9, 9, 9, 9, 9, 9, 9, 9],
          [9, 9, 9, 9, 9, 9, 9, 9, 9]]


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


def fill(bo):
    found = find_first_empty(bo)
    if not found:
        return True
    else:
        x = found[0]
        y = found[1]

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(nums)
    for i in range(0, 9):
        if valid(bo, nums[i], found):
            bo[x][y] = nums[i]

            if fill(bo):
                return True
            else:
                bo[x][y] = 0
    return False


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


def find_random_nonempty(bo):
    non_empty = []
    for i in range(9):
        for j in range(9):
            if bo[i][j] > 0:
                non_empty.append((i, j))

    if len(non_empty) == 0:
        return None

    return random.choice(non_empty)


def num_solutions_helper(bo, acc):
    if acc > 1:
        return 2

    copied = copy.deepcopy(bo)
    found = find_first_empty(copied)
    if not found:
        return 1
    else:
        row = found[0]
        col = found[1]

    for i in range(1, 10):
        if valid(copied, i, found):
            copied[row][col] = i
            acc += num_solutions_helper(copied, acc)
    return acc


def quant_sol(bo):
    cop = copy.deepcopy(bo)
    val = num_solutions_helper(cop, 0)
    if val > 1:
        return 2
    else:
        return val


def gen_board(num_cells):
    current = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    fill(current)
    while True:
        pos = find_random_nonempty(current)
        if not pos:
            break

        row = pos[0]
        col = pos[1]
        old_num = current[row][col]
        current[row][col] = 0
        if quant_sol(current) > 1:
            current[row][col] = old_num
            nonempty = get_all_nonempty(current)
            if len(nonempty) <= num_cells:
                break
            if not len(nonempty) == 0:
                random.shuffle(nonempty)
            more = False
            for cell in nonempty:
                c_row = cell[0]
                c_col = cell[1]
                c_old_num = current[c_row][c_col]
                current[c_row][c_col] = 0
                if quant_sol(current) > 1:
                    current[c_row][c_col] = c_old_num
                else:
                    if len(get_all_nonempty(current)) <= num_cells:
                        break
                    more = True
            if not more:
                break

    return current


def get_all_nonempty(bo):
    ret = []
    for i in range(9):
        for j in range(9):
            if not bo[i][j] == 0:
                ret.append((i, j))
    return ret

