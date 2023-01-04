import pygame
import random

global default_grid


level1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

level2 = [
    [0, 6, 0, 1, 0, 4, 0, 5, 0],
    [0, 0, 8, 3, 0, 5, 6, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 1],
    [8, 0, 0, 4, 0, 7, 0, 0, 6],
    [0, 0, 6, 0, 0, 0, 3, 0, 0],
    [7, 0, 0, 9, 0, 1, 0, 0, 4],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 7, 2, 0, 6, 9, 0, 0],
    [0, 4, 0, 5, 0, 8, 0, 7, 0]
]
level3 = [
    [0, 0, 0, 6, 0, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 3, 6, 0, 0],
    [0, 0, 0, 0, 9, 1, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 1, 8, 0, 0, 0, 3],
    [0, 0, 0, 3, 0, 6, 0, 4, 5],
    [0, 4, 0, 2, 0, 0, 0, 6, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 1, 0, 0]
]
level4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 8, 5],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 3],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9]
]


def cord(position):
    global x
    x = position[0] // diff
    global y
    y = position[1] // diff


def highlight_box():
    for k in range(2):  # Highlight for the selected box
        pygame.draw.line(Window, (0, 0, 0), (x * diff - 3, (y + k) * diff), (x * diff + diff + 3, (y + k) * diff), 7)
        pygame.draw.line(Window, (0, 0, 0), ((x + k) * diff, y * diff), ((x + k) * diff, y * diff + diff), 7)


def draw_lines():
    for i in range(9):
        for j in range(9):
            if default_grid[i][j] != 0:
                # Position of the squares
                pygame.draw.rect(Window, (220, 220, 220), (i * diff, j * diff, diff + 1, diff + 1))
                text1 = font.render(str(default_grid[i][j]), 1, (0, 0, 0))
                # Position of the numbers
                Window.blit(text1, (i * diff + 25, j * diff + 12))

    for l in range(10):
        if l % 3 == 0:
            thick = 6
        else:
            thick = 2
        # Every Line
        pygame.draw.line(Window, (0, 0, 0), (0, l * diff), (600, l * diff), thick)
        pygame.draw.line(Window, (0, 0, 0), (l * diff, 0), (l * diff, 600), thick)


def fillvalue(value):
    text1 = font.render(str(value), 1, (0, 0, 0))
    Window.blit(text1, (x * diff + 15, y * diff + 15))


def raiseerror():
    text1 = font1.render("Sudoku is Unsolvable Press 'R' To Restart", 1, (0, 0, 0))
    Window.fill((255, 255, 255))
    Window.blit(text1, (25, 255))
    pygame.display.update()
    pygame.time.delay(100)


def raiseerror1():
    text1 = font.render("You Can't Insert This Number", 1, (0, 0, 0))
    Window.fill((255, 255, 255))
    Window.blit(text1, (50, 255))
    pygame.display.update()
    pygame.time.delay(1000)


def valid_value(grid, k, l, value):
    # Checks for every line
    for it in range(9):
        if grid[k][it] == value:
            return False
        if grid[it][l] == value:
            return False
    # Checks for the 3x3 square
    it = k // 3
    jt = l // 3
    for k in range(it * 3, it * 3 + 3):
        for l in range(jt * 3, jt * 3 + 3):
            if grid[k][l] == value:
                return False
    return True


def solve_game(default_grid, i, j):
    pygame.event.pump()
    while default_grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    for it in range(1, 10):
        if valid_value(default_grid, i, j, it) == True:
            default_grid[i][j] = it
            global x, y
            x = i
            y = j

            """draw_lines()
            highlight_box()
            pygame.display.update()
            # pygame.time.delay(20)"""
            if solve_game(default_grid, i, j) == 1:
                return True
            else:
                default_grid[i][j] = 0

            """draw_lines()
            highlight_box()
            pygame.display.update()
            # pygame.time.delay(50)"""
    return False


def gameresult():
    Window.fill((255, 255, 255))
    text1 = font.render("Congrats! You Solved The Sudoku", 1, (0, 0, 0))
    Window.blit(text1, (50, 255))
    pygame.display.update()
    pygame.time.delay(5000)


def is_finished(lst):
    for row in lst:
        for element in row:
            if element == 0:
                return False
    return True


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def level_check(level):
    global default_grid
    if level == 5:
        level = random.randint(0, 4)
    if level == 1:
        default_grid = transpose(level1)
    elif level == 2:
        default_grid = transpose(level2)
    elif level == 3:
        default_grid = transpose(level3)
    else:
        default_grid = transpose(level4)


try:
    level = int(input("Enter a level\n1.Easy\n2.Medium\n3.Hard\n4.Impossible\n5.Random\n"))
except ValueError:
    level = int(input("1 - 2 - 3 - 4 Enter a number\n"))
level_check(level)



pygame.font.init()
Window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("SUDOKU GAME")
#  Coordinates
x = 0
y = 0

diff = 600 / 9  # For every square
value = 0


font = pygame.font.SysFont("bitstreamverasans", 40)
font1 = pygame.font.SysFont("bitstreamverasans", 35)



# For the main
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
while run:
    Window.fill((255, 255, 255))  # Background color
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_RETURN:
                if is_finished(default_grid):
                    rs = 1
            if event.key == pygame.K_1:
                value = 1
            if event.key == pygame.K_2:
                value = 2
            if event.key == pygame.K_3:
                value = 3
            if event.key == pygame.K_4:
                value = 4
            if event.key == pygame.K_5:
                value = 5
            if event.key == pygame.K_6:
                value = 6
            if event.key == pygame.K_7:
                value = 7
            if event.key == pygame.K_8:
                value = 8
            if event.key == pygame.K_9:
                value = 9
            if event.key == pygame.K_s:
                flag2 = 1
            if event.key == pygame.K_d:  # If you press "d" everything get back to default
                rs = 0
                error = 0
                flag2 = 0
                default_grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            if event.key == pygame.K_r:  # If you press "r" it set everything 0
                rs = 0
                error = 0
                flag2 = 0
                default_grid = [
                    [2, 5, 0, 0, 3, 0, 9, 0, 1],
                    [0, 1, 0, 0, 0, 4, 0, 0, 0],
                    [4, 0, 7, 0, 0, 0, 2, 0, 8],
                    [0, 0, 5, 2, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 9, 8, 1, 0, 0],
                    [0, 4, 0, 0, 0, 3, 0, 0, 0],
                    [0, 0, 0, 3, 6, 0, 0, 7, 2],
                    [0, 7, 0, 0, 0, 0, 0, 0, 3],
                    [9, 0, 3, 0, 0, 0, 6, 0, 4]
                ]
    if flag2 == 1:
        if solve_game(default_grid, 0, 0) == False:
            error = 1
        flag2 = 0
    if value != 0:
        # Insertion the valid number to the table and the list
        if valid_value(default_grid, int(x), int(y), value):
            default_grid[int(x)][int(y)] = value
            fillvalue(value)
            flag1 = 0
        else:
            default_grid[int(x)][int(y)] = 0
            raiseerror1()
        value = 0
    if error == 1:
        raiseerror()
    if rs == 1:
        gameresult()
        rs = 0
    if flag1 == 1:
        highlight_box()
    draw_lines()
    pygame.display.update()
pygame.quit()
