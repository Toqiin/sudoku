import copy

import pygame

from SudokuSolver import gen_solved

from gen_board import gen_board, print_board


def generate_cells(cells):
    ret = []
    for i in range(9):
        ret.append([])
        for j in range(9):
            num = cells[i][j]
            if num == 0:
                ret[i].append(Cell(num, True))
            else:
                ret[i].append(Cell(num, False))
    return ret


class Board:
    def __init__(self, cell_arr):
        self.cells = generate_cells(cell_arr)
        self.ini = list(cell_arr)
        self.solved = gen_solved(copy.deepcopy(self.ini))
        self.selected = None

    def set_cell(self, num, row, col):
        y = int(row)
        x = int(col)
        cell = self.cells[y][x]
        cell.set_num(num)

    def print_cells(self):
        for i in range(9):
            print("")
            for j in range(9):
                print(self.cells[i][j].num, end="  ")

    def draw_board(self, surface):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].draw_cell(surface, i, j)

    def load_board(self, to_load):
        self.cells = generate_cells(to_load)
        self.ini = list(to_load)
        self.solved = gen_solved(copy.deepcopy(self.ini))

    def select_pos(self, pos):
        row = int(pos[0])
        col = int(pos[1])
        cell = self.cells[row][col]
        if not self.selected:
            self.selected = pos
            cell.inv_selected()
        elif pos == self.selected:
            self.selected = None
            cell.inv_selected()
        else:
            old_row = int(self.selected[0])
            old_col = int(self.selected[1])
            old = self.cells[old_row][old_col]
            old.inv_selected()
            self.selected = pos
            cell.inv_selected()

    def update_select(self, num):
        if not self.selected:
            pass
        else:
            row = int(self.selected[0])
            col = int(self.selected[1])
            cell = self.cells[row][col]
            cell.set_num(num)


class Cell:
    def __init__(self, num, editable):
        self.num = num
        self.editable = editable
        self.selected = False

    def set_num(self, num):
        if self.editable:
            self.num = num

    def inv_selected(self):
        self.selected = not self.selected

    def draw_cell(self, surface, row, col):
        size = 60
        x = 0
        y = 0
        num = str(self.num)

        if col <= 2:
            x = 5 + (col * size) + (col * 3)
        elif 2 < col <= 5:
            x = 10 + (col * size) + ((col - 1) * 3)
        elif 5 < col <= 8:
            x = 15 + (col * size) + ((col - 2) * 3)

        if row <= 2:
            y = 5 + (row * size) + (row * 3)
        elif 2 < row <= 5:
            y = 10 + (row * size) + ((row - 1) * 3)
        elif 5 < row <= 8:
            y = 15 + (row * size) + ((row - 2) * 3)

        if self.selected:
            pygame.draw.rect(surface, (255, 0, 0), (x, y, size, size))
            pygame.draw.rect(surface, (255, 255, 255), (x + 3, y + 3, size - 6, size - 6))
        else:
            pygame.draw.rect(surface, (255, 255, 255), (x, y, size, size))

        if num != "0":
            font = pygame.font.SysFont('arial', 32)
            text = font.render(num, True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (x + size / 2, y + size / 2)
            surface.blit(text, text_rect)


board = [[1, 0, 8, 0, 0, 0, 0, 0, 3],
         [0, 0, 9, 8, 1, 0, 6, 0, 0],
         [0, 0, 6, 5, 2, 0, 0, 0, 0],
         [4, 7, 1, 9, 0, 2, 3, 0, 0],
         [0, 0, 3, 0, 4, 5, 0, 0, 0],
         [0, 0, 0, 0, 8, 1, 0, 6, 0],
         [3, 9, 7, 0, 0, 8, 0, 2, 4],
         [8, 6, 2, 1, 0, 0, 0, 0, 9],
         [0, 0, 0, 0, 3, 0, 7, 0, 6]]


def get_cell_from_pos(pos):
    x = pos[0] - 5
    y = pos[1] - 5
    print(x, y)
    row = -1
    col = -1

    def get_idx(int):
        cell = -1
        if 0 <= int <= 186:
            if not (int % 63 >= 60):
                cell = int // 60
                if cell == 3:
                    cell = 2
        elif 191 <= int <= 377:
            new_int = int - 191
            if not (new_int % 63 >= 60):
                cell = ((new_int // 60) + 3)
                if cell == 6:
                    cell = 5
        elif 382 <= int <= 568:
            new_int = int - 382
            if not (new_int % 63 >= 60):
                cell = ((new_int // 60) + 6)
                if cell == 9:
                    cell = 8
        return cell

    row = get_idx(y)
    col = get_idx(x)
    print(row, col)

    if row > -1 and col > -1:
        return row, col
    else:
        return None


def main():
    pygame.init()
    size = 578
    win = pygame.display.set_mode((size, size))
    flag = True
    b = Board(board)
    b.draw_board(win)

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                cell = get_cell_from_pos(pos)
                if cell:
                    b.select_pos(cell)
                    b.draw_board(win)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    b.update_select(0)
                elif event.key == pygame.K_1:
                    b.update_select(1)
                elif event.key == pygame.K_2:
                    b.update_select(2)
                elif event.key == pygame.K_3:
                    b.update_select(3)
                elif event.key == pygame.K_4:
                    b.update_select(4)
                elif event.key == pygame.K_5:
                    b.update_select(5)
                elif event.key == pygame.K_6:
                    b.update_select(6)
                elif event.key == pygame.K_7:
                    b.update_select(7)
                elif event.key == pygame.K_8:
                    b.update_select(8)
                elif event.key == pygame.K_9:
                    b.update_select(9)
                elif event.key == pygame.K_r:
                    b.load_board(gen_board(40))
                elif event.key == pygame.K_SPACE:
                    b.load_board(b.solved)
                b.draw_board(win)

        pygame.display.update()


main()
