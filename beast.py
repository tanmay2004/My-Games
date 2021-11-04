# Inspired by https://github.com/dominikwilkowski/beast.js
# Created by Tanmay Garg

import pygame, random
from pygame.locals import *

class Food:
    def set_collision(self):
        self.col_li = [[self.row, self.col-1], [self.row, self.col+1], [self.row-1, self.col], [self.row+1, self.col]]

    def start_pos(self):
        r, c = random.randint(2, 29), random.randint(2, 74)

        while grid_arr[r][c] != 0:
            r, c = random.randint(2, 29), random.randint(2, 74)

        grid_arr[r][c] = self.name
        return r, c

    def __init__(self, index, color=(139,0,139)):
        self.color = color
        self.name = "food" + str(index)
        self.row, self.col = self.start_pos()
        self.desroyed = False
        self.set_collision()

    def get_rand(self):
        arrx, arry = [-1, 0, 1], [-1, 0, 1]

        x = random.choice(arrx)
        if x == 0:
            arry.remove(0)
        y = random.choice(arry)

        return x, y

    def next_position(self):
        grid_arr[self.row][self.col] = 0
        dx, dy = self.get_rand()

        try:
            while grid_arr[self.row+dx][self.col+dy] != 0:
                dx, dy = self.get_rand()
        except IndexError:
            dx, dy = self.get_rand()

        self.row = max(0, min(self.row+dx, 29))
        self.col = max(0, min(self.col+dy, 74))

        self.set_collision()
        grid_arr[self.row][self.col] = self.name

    def destroy(self):
        self.desroyed = True


pygame.init()
font = pygame.font.SysFont('Helvetica', 40)
credit_f = pygame.font.SysFont('Helvetica', 20)

WIDTH, HEIGHT = 850, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0,0,0))
pygame.display.set_caption("Beast!")
clock = pygame.time.Clock()

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (34,139,34)
BLUE = (0,0,255)

lives = 3

def draw_setup():
    txt = font.render('BEAST', True, WHITE)
    textRect = txt.get_rect(center=(100, 50))
    screen.blit(txt, textRect)

    txt2 = credit_f.render('Created By Tanmay Garg', True, WHITE)
    textRect2 = txt2.get_rect(center=(700, 50))
    screen.blit(txt2, textRect2)

    txt3 = credit_f.render('Lives Remaining: ' + str(lives), True, WHITE)
    textRect3 = txt3.get_rect(center=(120, 572))
    screen.blit(txt3, textRect3)

def get_within_boundary():
    global x, y
    x = min(790, max(x, 50))
    y = min(530, max(y, 95))

x, y = 50, 95
fps_time = 0

a_list = [0, 1]
distribution = [.8, .2]

running = True
rows, cols = 30, 75 # 30x75 2d array
grid_arr = [[random.choices(a_list, distribution)[0] for i in range(cols)] for j in range(rows)]
grid_arr[0][0] = None # initial player position

food_li = [Food(x) for x in range(5)]

while running:
    fps_time += 1
    keys = pygame.key.get_pressed()
    c, r = (x-50) // 10, (y-95) // 15

    if keys[K_LEFT]:
        c -= 1

        try:
            while grid_arr[r][c] == 1:
                c -= 1
                if c == -1:
                    raise IndexError
            else:
                if "food" in str(grid_arr[r][c]):
                    f = food_li[int(grid_arr[r][c][-1])]

                    if c-1 == -1 or grid_arr[r][c-1]:
                        f.destroy()
                    else:
                        f.col -= 1
                        grid_arr[r][c-1] = f.name
                grid_arr[r][c] = 1
            x -= 10
        except:
            pass

        grid_arr[(y-95) // 15][(x-50) // 10] = None

    elif keys[K_RIGHT]:
        c += 1

        try:
            while grid_arr[r][c] == 1:
                c += 1
            else:
                if "food" in str(grid_arr[r][c]):
                    f = food_li[int(grid_arr[r][c][-1])]

                    if c+1 == 75 or grid_arr[r][c+1]:
                        f.destroy()
                    else:
                        f.col += 1
                        grid_arr[r][c+1] = f.name
                grid_arr[r][c] = 1
            x += 10
        except:
            pass

        grid_arr[(y-95) // 15][(x-50) // 10] = None

    elif keys[K_UP]:
        r -= 1

        try:
            while grid_arr[r][c] == 1:
                r -= 1
                if r == -1:
                    raise IndexError
            else:
                if "food" in str(grid_arr[r][c]):
                    f = food_li[int(grid_arr[r][c][-1])]

                    if r-1 == -1 or grid_arr[r-1][c]:
                        f.destroy()
                    else:
                        f.row -= 1
                        grid_arr[r-1][c] = f.name
                grid_arr[r][c] = 1
            y -= 15
        except:
            pass

        grid_arr[(y-95) // 15][(x-50) // 10] = None

    elif keys[K_DOWN]:
        r += 1

        try:
            while grid_arr[r][c] == 1:
                r += 1
            else:
                if "food" in str(grid_arr[r][c]):
                    f = food_li[int(grid_arr[r][c][-1])]

                    if r+1 == 30 or grid_arr[r+1][c]:
                        f.destroy()
                    else:
                        f.row += 1
                        grid_arr[r+1][c] = f.name
                grid_arr[r][c] = 1
            y += 15

        except:
            pass

        grid_arr[(y-95) // 15][(x-50) // 10] = None

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill(BLACK)

    for f in food_li:
        if not f.desroyed:
            if fps_time % 30 == 0:
                f.next_position()
            pygame.draw.rect(screen, f.color, (50+10*f.col, 95+15*f.row, 10, 15))

            f.set_collision()
            if [(y-95) // 15, (x-50) // 10] in f.col_li:
                lives -= 1
                f.row, f.col = f.start_pos()
                x, y = 50, 95
                fps_time = 0

    get_within_boundary()
    draw_setup()

    pygame.draw.rect(screen, BLUE, (x, y, 10, 15))
    pygame.draw.rect(screen, WHITE, (48, 93, 753, 453), 2)

    for row in range(rows):
        for col in range(cols):
            if grid_arr[row][col] == 1:
                pygame.draw.rect(screen, GREEN, (50+10*col, 95+15*row, 10, 15))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
