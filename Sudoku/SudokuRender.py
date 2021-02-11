import pygame

from SudokuSolver import solve

pygame.init()

board = [[1, 0, 8, 0, 0, 0, 0, 0, 3],
         [0, 0, 9, 8, 1, 0, 6, 0, 0],
         [0, 0, 6, 5, 2, 0, 0, 0, 0],
         [4, 7, 1, 9, 0, 2, 3, 0, 0],
         [0, 0, 3, 0, 4, 5, 0, 0, 0],
         [0, 0, 0, 0, 8, 1, 0, 6, 0],
         [3, 9, 7, 0, 0, 8, 0, 2, 4],
         [8, 6, 2, 1, 0, 0, 0, 0, 9],
         [0, 0, 0, 0, 3, 0, 7, 0, 6]]


def draw_board(surface, bo):
    for i in range(9):
        for j in range(9):
            draw_cell(surface, i, j, bo)


def draw_cell(surface, row, col, bo):
    size = 60
    x = 0
    y = 0
    num = str(bo[row][col])

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

    pygame.draw.rect(surface, (255, 255, 255), (x, y, size, size))

    if num != "0":
        font = pygame.font.SysFont('arial', 32)
        text = font.render(num, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (x + size / 2, y + size / 2)
        surface.blit(text, text_rect)


def main():
    size = 578
    win = pygame.display.set_mode((size, size))
    flag = True
    draw_board(win, board)

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            print("tst")
            solve(board)
            draw_board(win, board)

        pygame.display.update()


main()
