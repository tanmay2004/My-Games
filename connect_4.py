import pygame, time
from pygame.locals import *

class Disc:
    def __init__(self, x, y, r=25):
        self.filled = False
        self.r = r
        self.x = 80+60*x
        self.y = 140+60*y
        self.color = (0,0,0)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def set_color(self, color):
        self.color = color

print("\nCONTROLS:")
print("1. Use arrow keys to navigate the columns")
print("2. Press the enter key to finish your move\n")

time.sleep(2)
pygame.init()

WIDTH, HEIGHT = 520, 520
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Play Connect 4!")
font = pygame.font.SysFont("helvetica", 40)
clock = pygame.time.Clock()

BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

d = {0: RED, 1: YELLOW}
d2 = {0: "Red", 1: "Yellow"}
message = "DRAW! Thanks for playing!"

matrix = []

for i in range(7):
    curr = []
    for j in range(6):
        curr.append(Disc(i, j))
    matrix.append(curr)

running = True
column = 3
turn_col = 0
moves_num = 0

def check_win(x, y, col):

    # Downwards
    count = 1
    for i in range(y+1, 6):
        if matrix[x][i].color == col:
            count += 1
            if count == 4:
                return True
        else:
            break

    # Left Row
    c_left = 0
    for i in range(x-1, -1, -1):
        if matrix[i][y].color == col:
            c_left += 1
        else:
            break

    # Right Row
    c_right = 1
    for i in range(x+1, 7):
        if matrix[i][y].color == col:
            c_right += 1
        else:
            break

    if c_left+c_right >= 4:
        return True

    # Diagonal 1
    c_left = 0
    for i in range(1, min(x, y)+1):
        if matrix[x-i][y-i].color == col:
            c_left += 1
        else:
            break

    c_right = 1
    for i in range(1, min(6-x, 5-y)+1):
        if matrix[x+i][y+i].color == col:
            c_right += 1
        else:
            break

    if c_left+c_right >= 4:
        return True

    # Diagonal 2
    c_left = 0
    for i in range(1, min(x, 5-y)+1):
        if matrix[x-i][y+i].color == col:
            c_left += 1
        else:
            break

    c_right = 1
    for i in range(1, min(6-x, y)+1):
        if matrix[x+i][y-i].color == col:
            c_right += 1
        else:
            break

    if c_left+c_right >= 4:
        return True

    return False

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RETURN:
                if not matrix[column][0].filled:
                    row = None
                    moves_num += 1

                    for num in range(6):
                        if matrix[column][num].filled:
                            matrix[column][num-1].set_color(d[turn_col])
                            matrix[column][num-1].filled = True
                            row = num-1
                            break
                        elif num == 5:
                            matrix[column][num].set_color(d[turn_col])
                            matrix[column][num].filled = True
                            row = num

                    if moves_num >= 7 and check_win(column, row, d[turn_col]):
                        print(d2[turn_col] + " wins! Congrats!")
                        print("Game over! Exiting...")
                        message = d2[turn_col]+" wins! Thanks for playing!"
                        running = False

                    turn_col = not turn_col

                    if moves_num == 42:
                        running = False

            elif event.key == K_LEFT:
                column = max(0, column-1)
            elif event.key == K_RIGHT:
                column = min(6, column+1)

    pygame.draw.rect(screen, BLUE, (45, 105, 430, 370))

    if running:
        pygame.draw.circle(screen, d[turn_col], (80+60*column, 70), 25)
    else:
        txt = font.render(message, True, WHITE)
        textRect = txt.get_rect(center=(260, 50))
        screen.blit(txt, textRect)

    for el in matrix:
        for disc in el:
            disc.draw()

    pygame.display.update()
    clock.tick(60)

time.sleep(5)
pygame.quit()
print("Goodbye!")
