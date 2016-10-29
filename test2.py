import pygame
from pygame.color import Color

(width,height) = (640,480)
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('Hack Sim')

background_color = Color("pink")
screen.fill(background_color)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False