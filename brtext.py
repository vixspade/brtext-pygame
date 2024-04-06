# IMPORT
import pygame
from pygame.locals import *
import random
import time

# INIT VARS
colour = (255, 255, 255)
w = 1900
h = 880
size = 48
lineoff = (size / 2) + 10
dt = time.perf_counter()

# INIT PYGAME + FONTS
pygame.init()
screen = pygame.display.set_mode((w, h))
font = pygame.font.SysFont('fakereceiptregular', size)

line1 = "NOW THE SHOW IS ALL YOURS ."
line2 = "WHAT DO YOU HAVE TO SAY ?"
text1 = ''
text2 = ''
# START GAME
running = True
input()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    if time.perf_counter() - dt >= 0.03:
        if len(text1) < len(line1):
            text1 += line1[len(text1)]
        elif len(text2) < len(line2):
            text2 += line2[len(text2)]
        dt = time.perf_counter()
    offsetx = random.randint(0, 2) - 1
    offsety = random.randint(0, 2) - 1
    screen.fill((0, 0, 0))
    img1 = font.render(text1, False, colour)
    img2 = font.render(text2, False, colour)
    rect1 = img1.get_rect()
    rect2 = img2.get_rect()
    rect1.center = (w/2 + offsetx, h/2 + offsety - lineoff)
    rect2.center = (w / 2 + offsetx, h / 2 + offsety + lineoff)
    screen.blit(img1, rect1)
    screen.blit(img2, rect2)
    pygame.display.update()


pygame.quit()
