import pygame, random, sys
from pygame.locals import *

def adjust_random(pos):
    adjusted_pos = pos.copy()
    for k in range(2):
        if pos[k] > 600:
            adjusted_pos[k] = pos[k] - 2
        elif pos[k] < 0:
            adjusted_pos[k] = pos[k] + 2
    return adjusted_pos

def get_new_loc(pos):
    pos_li = list(pos)
    pos_li[0] += random.choice([-1, 1])
    pos_li[1] += random.choice([-1, 1])
    pos_li = adjust_random(pos_li)
    return tuple(pos_li)

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = int(input("\nEnter your desired brush width: "))
filename = input("Enter a filename to save your random walk: ")

print("\nYou can end the walk using the ESC key to see it saved as an image!")
pygame.display.set_caption("Random Walker")
screen = pygame.display.set_mode((600, 600), 0, 32)
screen.fill(WHITE)

last_pos = (300, 300)
mouse_position = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    mouse_position = get_new_loc(last_pos)
    pygame.draw.line(screen, BLACK, last_pos, mouse_position, WIDTH)

    last_pos = mouse_position
    pygame.display.update()

pygame.image.save(screen, filename)
pygame.quit()
sys.exit()
